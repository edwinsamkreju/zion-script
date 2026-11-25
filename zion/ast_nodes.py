"""Abstract syntax tree nodes."""
from dataclasses import dataclass

@dataclass
class Program: statements: list
@dataclass
class Store: name: str; value: str; line: int
@dataclass
class Say: value: str; line: int
@dataclass
class Ask: prompt: str; name: str; line: int
@dataclass
class Math: operation: str; left: str; right: str; line: int
@dataclass
class If: branches: list; otherwise: list | None; line: int
@dataclass
class Repeat: count: str; body: list; line: int
@dataclass
class ForEach: item: str; collection: str; body: list; line: int
@dataclass
class CreateList: name: str; line: int
@dataclass
class AddToList: value: str; name: str; line: int
@dataclass
class Function: name: str; body: list; line: int
@dataclass
class RunFunction: name: str; line: int
