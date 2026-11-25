"""Command-line interface for ZION SCRIPT."""
import argparse
import sys
from pathlib import Path
from zion import __version__
from zion.compiler import transpile
from zion.errors import ZionError

def main(argv=None):
    parser = argparse.ArgumentParser(prog="zion", description="Compile and run ZION SCRIPT programs.")
    parser.add_argument("--version", action="version", version=f"ZION SCRIPT {__version__}")
    commands = parser.add_subparsers(dest="command", required=True)
    run_cmd = commands.add_parser("run", help="Compile and run a .zion file")
    run_cmd.add_argument("file")
    py_cmd = commands.add_parser("transpile", help="Print generated Python code")
    py_cmd.add_argument("file")
    args = parser.parse_args(argv)
    try:
        path = Path(args.file)
        source = path.read_text(encoding="utf-8")
        python_source = transpile(source)
        if args.command == "transpile": print(python_source, end="")
        else:
            # This is not a sandbox. Do not run untrusted ZION files.
            exec(compile(python_source, str(path) + " [generated Python]", "exec"), {"__name__": "__main__"})
        return 0
    except (OSError, ZionError, SyntaxError) as exc:
        print(f"ZION error: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__": raise SystemExit(main())
