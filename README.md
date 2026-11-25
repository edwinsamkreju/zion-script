# ZION SCRIPT

**Simple language. Unlimited possibilities.**

ZION SCRIPT is an experimental, beginner-friendly programming language with simple English-inspired commands. It transpiles `.zion` source files into Python and runs the generated program.

> Status: early prototype (v0.1.0). The syntax and implementation may change.

## Quick start

Requires Python 3.10 or newer.

```bash
python -m zion run examples/hello.zion
python -m zion transpile examples/hello.zion
```

## Example

```text
Store 10 as number

If number is greater than 5
    Say "Hello from ZION!"
Otherwise
    Say "Keep learning!"
End if
```

## Features in v0.1

- Variables, output and input
- Arithmetic and friendly comparison phrases
- Conditions and repetition
- Lists and for-each loops
- Simple functions
- Python transpilation and command-line interface

See [docs/SYNTAX.md](docs/SYNTAX.md).

## Tests

```bash
python -m unittest discover -s tests -v
```

## Safety

This prototype is not a secure sandbox. Generated Python has the same permissions as the Python process. Only run programs you trust.

## License

MIT. See [LICENSE](LICENSE).
