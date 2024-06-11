from Models.Studium import Studium


class CourseServiceInterface:
    def get_studium(self, studiumId: str) -> Studium:
        pass

    def get_all(self):
        pass