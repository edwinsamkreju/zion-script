"""Recursive-descent parser for ZION SCRIPT."""
import ast
import re
from zion.ast_nodes import *
from zion.errors import ZionError
from zion.lexer import lex, SourceLine

class Parser:
    def __init__(self, lines: list[SourceLine]): self.lines, self.pos = lines, 0
    def parse(self):
        result = self.block(0, set())
        if self.pos < len(self.lines):
            raise ZionError("Unexpected indentation. Check the spaces before this command.", self.lines[self.pos].number)
        return Program(result)
    def block(self, indent, endings):
        out = []
        while self.pos < len(self.lines):
            line = self.lines[self.pos]
            if line.indent < indent: break
            if line.indent > indent:
                raise ZionError("This line is indented more than expected.", line.number)
            if line.text.lower() in {x.lower() for x in endings}: break
            out.append(self.statement(indent))
        return out
    def nested(self, parent_indent, endings, opener):
        if self.pos >= len(self.lines) or self.lines[self.pos].indent <= parent_indent:
            raise ZionError("Add an indented command inside this block.", opener.number)
        return self.block(self.lines[self.pos].indent, endings)
    def expect(self, ending, opener):
        if self.pos >= len(self.lines) or self.lines[self.pos].text.lower() != ending.lower():
            raise ZionError(f"Missing '{ending}' for the block that starts here.", opener.number)
        self.pos += 1
    def statement(self, indent):
        line = self.lines[self.pos]
        self.pos += 1
        text = line.text
        m = re.fullmatch(r"Store\s+(.+)\s+as\s+([A-Za-z_]\w*)", text, re.I)
        if m: return Store(m.group(2), m.group(1), line.number)
        m = re.fullmatch(r"([A-Za-z_]\w*)\s+be\s+(.+)", text, re.I)
        if m: return Store(m.group(1), m.group(2), line.number)
        if re.fullmatch(r"[A-Za-z_]\w*\s*=\s*(?!=).+", text):
            return PythonStatement(text, line.number)
        m = re.fullmatch(r"(?:Show|Say)\s+(.+)", text, re.I)
        if m: return Say(m.group(1), line.number)
        m = re.fullmatch(r'Ask\s+(.+?)\s+and\s+store\s+the\s+answer\s+as\s+([A-Za-z_]\w*)', text, re.I)
        if m:
            if not (m.group(1).startswith(('"', "'")) and m.group(1)[-1:] == m.group(1)[:1]):
                raise ZionError("Put the input question inside quotation marks.", line.number)
            return Ask(m.group(1), m.group(2), line.number)
        patterns = [
            (r"Add\s+(.+)\s+and\s+(.+)", "add"),
            (r"Subtract\s+(.+)\s+from\s+(.+)", "subtract"),
            (r"Multiply\s+(.+)\s+and\s+(.+)", "multiply"),
            (r"Divide\s+(.+)\s+by\s+(.+)", "divide"),
        ]
        for pattern, op in patterns:
            m = re.fullmatch(pattern, text, re.I)
            if m:
                a, b = m.groups()
                if op == "subtract": a, b = b, a
                return Math(op, a, b, line.number)
        if re.match(r"If\s+", text, re.I): return self.parse_if(indent, line)
        m = re.fullmatch(r"Repeat\s+(.+)\s+times", text, re.I)
        if m:
            body = self.nested(indent, {"End repeat"}, line)
            self.expect("End repeat", line)
            return Repeat(m.group(1), body, line.number)
        m = re.fullmatch(r"For each\s+([A-Za-z_]\w*)\s+in\s+([A-Za-z_]\w*)", text, re.I)
        if m:
            body = self.nested(indent, {"End for"}, line)
            self.expect("End for", line)
            return ForEach(m.group(1), m.group(2), body, line.number)
        m = re.fullmatch(r"Create a list called\s+([A-Za-z_]\w*)", text, re.I)
        if m: return CreateList(m.group(1), line.number)
        m = re.fullmatch(r"Add\s+(.+)\s+to\s+([A-Za-z_]\w*)", text, re.I)
        if m: return AddToList(m.group(1), m.group(2), line.number)
        m = re.fullmatch(r"Create a function called\s+([A-Za-z_]\w*)", text, re.I)
        if m:
            body = self.nested(indent, {"End function"}, line)
            self.expect("End function", line)
            return Function(m.group(1), body, line.number)
        m = re.fullmatch(r"Run\s+([A-Za-z_]\w*)", text, re.I)
        if m: return RunFunction(m.group(1), line.number)
        # Python statements and expressions pass through for ecosystem interoperability.
        try:
            ast.parse(text, mode="exec")
        except SyntaxError as exc:
            raise ZionError(f"I don't understand '{text}'. Check the command spelling or syntax.", line.number) from exc
        return PythonStatement(text, line.number)
    def parse_if(self, indent, opener):
        condition = re.sub(r"^If\s+", "", opener.text, flags=re.I)
        branches = [(condition, self.nested(indent, {"Otherwise", "End if"}, opener))]
        otherwise = None
        while self.pos < len(self.lines) and self.lines[self.pos].indent == indent:
            marker = self.lines[self.pos]
            m = re.fullmatch(r"Otherwise\s+if\s+(.+)", marker.text, re.I)
            if m:
                self.pos += 1
                branches.append((m.group(1), self.nested(indent, {"Otherwise", "End if"}, marker)))
            elif marker.text.lower() == "otherwise":
                self.pos += 1
                otherwise = self.nested(indent, {"End if"}, marker)
                break
            else: break
        self.expect("End if", opener)
        return If(branches, otherwise, opener.number)

def parse(source: str): return Parser(lex(source)).parse()
