from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from Models.Student import Student


class ModuleECTS:

    __console : Console

    def __init__(self, console: Console) -> None:
        self.__console = console

    def render(self, student : Student):
        ects = 0
        total = 0
        for mod in student.EingeschriebenesStudium.Module:
            if(mod.passed() == "JA"):
                ects += mod.ECTS
            total += mod.ECTS

        pnl = Panel(f"Erreichte ECTS: {ects} von {total}", title="Ziel 1", expand=True)
        self.__console.print(pnl)