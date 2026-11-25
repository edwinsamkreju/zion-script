# ZION SCRIPT language design

## Goals

1. Make the first programming experience approachable for school students.
2. Use consistent, readable, English-inspired statements.
3. Compile to Python to benefit from its ecosystem.
4. Keep the language small and predictable before adding advanced features.

## Non-goals for v0.1

- Understanding arbitrary natural-language instructions.
- Full Python syntax compatibility.
- Secure execution of untrusted programs.
- Static type inference or compiler optimization.

## Compiler pipeline

`.zion` source -> lexer -> parser -> abstract syntax tree (AST) -> Python code generator -> Python runtime.

The lexer preserves source line numbers and indentation. The parser builds AST nodes. Code generation runs only after parsing succeeds.

## Design decisions

- Keywords are case-insensitive in v0.1.
- Identifiers use Python-style names and are case-sensitive.
- Four spaces are recommended for indentation.
- Blank lines and lines beginning with `#` are ignored.
- Expressions use a limited Python-compatible expression subset plus friendly comparison phrases.
