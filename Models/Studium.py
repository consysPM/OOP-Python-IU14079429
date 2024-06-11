from dataclasses import dataclass
from dataclasses import field
from Models.Modul import Modul



@dataclass
class Studium:
    StudiumId: str
    Name: str
    Module: list[Modul] = field(default_factory=list)