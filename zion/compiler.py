"""Public ZION compiler API."""
from zion.parser import parse
from zion.codegen import generate

def transpile(source: str) -> str:
    """Compile ZION source text into Python source text."""
    return generate(parse(source))
