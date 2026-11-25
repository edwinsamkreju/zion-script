"""Indentation-aware source-line lexer for ZION v0.1."""
from dataclasses import dataclass

@dataclass(frozen=True)
class SourceLine:
    number: int
    indent: int
    text: str

def lex(source: str) -> list[SourceLine]:
    lines = []
    for number, raw in enumerate(source.splitlines(), 1):
        expanded = raw.expandtabs(4)
        if not expanded.strip() or expanded.lstrip().startswith("#"):
            continue
        indent = len(expanded) - len(expanded.lstrip(" "))
        lines.append(SourceLine(number, indent, expanded.strip()))
    return lines
