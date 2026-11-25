# ZION SCRIPT

**Simple to read. Powered by Python.**

ZION SCRIPT is an experimental, beginner-friendly language with English-inspired commands. It transpiles .zion files into Python and uses Python's runtime and ecosystem.

> Status: early prototype (v0.1.0). The language is evolving; not every Python construct has a dedicated ZION spelling.

## Quick start

Requires Python 3.10 or newer.

\`\`\`bash
python -m zion run examples/hello.zion
python -m zion transpile examples/hello.zion
python -m unittest discover -s tests -v
\`\`\`

## Example

\`\`\`zion
show "Hello, world!"
marks be 100
average = 85.5

if marks >= 90
    show "Excellent!"
otherwise
    show "Keep learning!"
end if

repeat 3 times
    show "Hello again!"
end repeat
\`\`\`

## Language decisions

- show replaces Say for output.
- name be value assigns a variable.
- name = value is also supported.
- == compares values; = assigns values, matching Python.
- Python arithmetic, comparison, boolean, bitwise, identity, membership and augmented-assignment operators are supported through Python-compatible expressions/statements.
- Python imports, calls and statements can pass through the transpiler, providing access to installed libraries.
- The original Store/Say syntax remains accepted for compatibility.

See docs/SYNTAX.md for the syntax guide. The compiler uses a lexer, recursive-descent parser, AST, Python code generator and AST validation.

## Safety

This prototype is not a secure sandbox. Generated Python has the same permissions as the Python process. Only run programs you trust.

## Website

The landing page is in the repository root (index.html and styles.css), ready for GitHub Pages. The source copy is also in website/. To publish, open Settings → Pages, select Deploy from a branch, choose main and /(root), then save. Publishing must be enabled by a repository administrator.

## License

MIT. See LICENSE.
