from Interfaces.CourseServiceInterface import CourseServiceInterface
import csv
import os

from Models.Studium import Studium
from Models.Modul import Modul


class CsvCourseService(CourseServiceInterface):
     CSV_FILE_STUDIEN = "studien.csv"
     CSV_FILE_MODULE = "module.csv"

     __studien = list[Studium]
     __proj_dir: str
     def __init__(self, proj_dir: str):
         self.__proj_dir = proj_dir

     def get_studium(self, studiumId: str) -> Studium:
         for studium in self.__studien:
            if(studium.StudiumId == studiumId):
               return studium
         return None
     
     def get_all(self):
        return self.__studien
     
     def load(self):
         studienArr = []
         studienPath = os.path.join(self.__proj_dir, CsvCourseService.CSV_FILE_STUDIEN)
         modulePath = os.path.join(self.__proj_dir, CsvCourseService.CSV_FILE_MODULE)

         with open(studienPath, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                studiumObj = Studium(row["StudiumId"], row["Name"])
                studienArr.append(studiumObj)
         
         with open(modulePath, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                moduleObj = Modul(row["StudiumId"], row["ModulName"], row["ModulCode"], float(row["ECTS"]))
                for studium in studienArr:
                    if studium.StudiumId == moduleObj.StudiumId:
                        studium.Module.append(moduleObj)
         
         self.__studien = studienArr
                  

            