import argparse
from Dashboard.ModuleAvgGrade import ModuleAvgGrade
from Dashboard.ModuleECTS import ModuleECTS
from Dashboard.ModuleTable import ModuleTable
from Interfaces.CourseServiceInterface import CourseServiceInterface
from Interfaces.StudentServiceInterface import StudentServiceInterface
from Models.Student import Student
from Models.Studium import Studium
from rich.console import Console
from rich.prompt import Prompt
from rich.prompt import FloatPrompt


class StudentDashboard:

    __courseService: CourseServiceInterface
    __studentService: StudentServiceInterface
    __sel_student = Student
    __table: ModuleTable
    __ects: ModuleECTS
    __avg_grade: ModuleAvgGrade
    __console: Console

    def __init__(self, courseService: CourseServiceInterface, studentService: StudentServiceInterface) -> None:
        self.__courseService = courseService
        self.__studentService = studentService
        self.__console = Console()
        self.__table = ModuleTable(self.__console)    
        self.__ects = ModuleECTS(self.__console)
        self.__avg_grade = ModuleAvgGrade(self.__console)

    def enrole(self, matrikelNr, studiumId):
        sel_student : Student = self.__studentService.get_student(matrikelNr)
        sel_studium : Studium = self.__courseService.get_studium(studiumId)
        sel_student.EingeschriebenesStudium = sel_studium

        self.__sel_student = sel_student
        self.__studentService.init_grades(sel_student)

    def set_target_grade(self, grade: float):
        self.__avg_grade.set_target_grade(grade)
    
    def run(self):
        input = ""
        self.render()
        while input != "quit":
            input = self.__console.input(f"dashboard@[green]{self.__sel_student.MatrikelNr}[/green]>")
            args = input.split()

            if(len(args) > 0):
                cmd = args[0]
                if(cmd == "note"):
                    try:
                        module_choices = list(map(lambda x: f"{x.ModuleCode}", self.__sel_student.EingeschriebenesStudium.Module))
                        sel_mod_code = Prompt.ask("Wählen sie ein Modul aus", choices=module_choices)
                        note = 100.0

                        while(note > 5.0):
                            note = FloatPrompt.ask("Mit welcher Note haben Sie das Modul abgeschlossen?")
                            if(note < 1.0):
                                note = 0.0

                        self.update_note(sel_mod_code, note)
                        self.__studentService.save_student(self.__sel_student)
                        self.render()
                    except:
                        self.__console.print("Bitte geben sie eine gültige Note bzw. ModuleCode ein")

    def update_note(self, module_code: str, note: float):
        for module in self.__sel_student.EingeschriebenesStudium.Module:
            if(module.ModuleCode == module_code):
                module.Note = note
                return
        raise "ModuleCode not found"

    def render(self):
        #UI
        self.__table.render(self.__sel_student)
        self.__ects.render(self.__sel_student)
        self.__avg_grade.render(self.__sel_student)
        self.__console.print("Verfügbare Befehle: quit(Beendet das Programm), note(Erlaubt die Eingabe einer Note für das angegebene Modul)")


