import csv
import os

from Interfaces.StudentServiceInterface import StudentServiceInterface
from Models.Student import Student
from Models.Studium import Studium
from Models.Modul import Modul


class CsvStudentService(StudentServiceInterface):
     CSV_FILE_STUDENTEN = "studenten.csv"

     __studenten = list[Student]
     __proj_dir : str
     def __init__(self, proj_dir: str):
         self.__proj_dir = proj_dir
     
     def get_all(self):
        return self.__studenten
     
     def get_student(self, matrikelNr: str):
         for student in self.__studenten:
             if(student.MatrikelNr == matrikelNr):
                return student
         return None
     
     def __get_student_savefile_name(self, student: Student):
         return os.path.join(self.__proj_dir, student.MatrikelNr + "_" + student.EingeschriebenesStudium.StudiumId + ".csv")
     
     def save_student(self, student: Student):
        path = self.__get_student_savefile_name(student)
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=["ModuleCode", "Note"])
            writer.writeheader()
            for mod in student.EingeschriebenesStudium.Module:
                writer.writerow({'ModuleCode': mod.ModuleCode, 'Note': str(mod.Note)})

     def init_grades(self, student: Student):
        path = self.__get_student_savefile_name(student)
        if os.path.exists(path):
            with open(path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    code = row["ModuleCode"]
                    for mod in student.EingeschriebenesStudium.Module:
                        if(mod.ModuleCode == code):
                            mod.Note = float(row["Note"])
         
     
     def load(self):
         studienArr = []
         path = os.path.join(self.__proj_dir, CsvStudentService.CSV_FILE_STUDENTEN)

         with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                studentObj = Student(row["StudentName"], row["MatrikelNr"])
                studienArr.append(studentObj)
         
         self.__studenten = studienArr
                  

            