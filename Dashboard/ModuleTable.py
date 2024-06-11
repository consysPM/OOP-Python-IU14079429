from rich import print
from rich.console import Console
from rich.table import Table

from Models.Student import Student


class ModuleTable:

    __console : Console

    def __init__(self, console: Console) -> None:
        self.__console = console

    def render(self, student : Student):
        table = Table(title = "Eingeschriebene Module")
        table.add_column("Code")
        table.add_column("Modul")
        table.add_column("ECTS")
        #table.add_column("Bestanden am")
        table.add_column("Note")
        table.add_column("Bestanden", justify="center")
        table.expand = True
        #self.__table.add_row("CODE-X", "Modul ", "5", "1,0", "[bold green]JA[/bold green]")
        for mod in student.EingeschriebenesStudium.Module:
            table.add_row(mod.ModuleCode, mod.ModuleName, str(mod.ECTS), str(mod.Note), mod.passed())
        self.__console.print(table)