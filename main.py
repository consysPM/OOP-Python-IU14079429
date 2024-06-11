import os
from CSV.CsvCourseService import CsvCourseService
from CSV.CsvStudentService import CsvStudentService
from rich.prompt import Prompt
from rich.prompt import IntPrompt
from StudentDashboard import StudentDashboard

data_dir = os.path.join( os.path.dirname(__file__), "_data")

#lade studien
studium_service = CsvCourseService(data_dir)
studium_service.load()

#lade studenten
studenten_service = CsvStudentService(data_dir)
studenten_service.load()

session = StudentDashboard(studium_service, studenten_service)

#prompt: wähle studenten aus
alle_studenten = list(map(lambda x: f"{x.MatrikelNr}", studenten_service.get_all()))
sel_matrikel_nr = Prompt.ask("Wählen sie eine zu überwachende MatrikelNr (Studenten) aus. (Enter für Standardauswahl)", choices=alle_studenten, default=alle_studenten[0])
#prompt: wähle ein studium aus
alle_studien = list(map(lambda x: f"{x.StudiumId}", studium_service.get_all()))
sel_studium_code = Prompt.ask("Wählen sie ein Studium aus. (Enter für Standardauswahl)", choices=alle_studien, default=alle_studien[0])

#prompt: frage zielergebnis (zielnote)
target_grade = IntPrompt.ask("Welche Gesamtnote ist ihr Zielergebnis?", choices=["1","2","3","4"], default=1)
#student in kurs einschreiben
session.enrole(sel_matrikel_nr, sel_studium_code)
session.set_target_grade(target_grade)

session.run()

print("bye!")

