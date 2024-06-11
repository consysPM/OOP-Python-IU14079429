from Models.Student import Student
from Models.Studium import Studium


class StudentServiceInterface:
    
    def get_all(self):
        pass

    def get_student(self, matrikelNr: str):
        pass

    def save_student(self, student: Student):
        pass
    def init_grades(self, student: Student):
        pass