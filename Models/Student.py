from dataclasses import dataclass
from dataclasses import field
from Models.Modul import Modul
from Models.Studium import Studium
from typing import Optional


@dataclass
class Student:
    Name: str
    MatrikelNr: str
    EingeschriebenesStudium: Optional[Studium] = None

