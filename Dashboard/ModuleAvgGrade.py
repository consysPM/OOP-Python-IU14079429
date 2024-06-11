from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from Models.Student import Student


class ModuleAvgGrade:

    __console : Console
    __target_grade: float = 1
    def __init__(self, console: Console) -> None:
        self.__console = console

    def set_target_grade(self, grade: float):
        self.__target_grade = grade

    def render(self, student : Student):
        grades = 0
        total = 0
        for mod in student.EingeschriebenesStudium.Module:
            if(mod.passed() == "JA" or mod.passed() == "NEIN"):
                total += mod.Note
                grades += 1

        if(grades > 0):
            avg = (total/grades)
            pnl = Panel(f"Ihre Durchschnittsnote: {avg:.2f} ({avg - self.__target_grade:.2f} vom Zielergebnis entfernt). Zielnote: {self.__target_grade}", title="Ziel 2", expand=True)
        else:
            pnl = Panel("Noch keine Benotung", title="Ziel 2", expand=True)
        self.__console.print(pnl)