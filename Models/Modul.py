from dataclasses import dataclass


@dataclass
class Modul:
    StudiumId: str
    ModuleName: str
    ModuleCode: str
    ECTS: float
    Note: float = 0.0

    def passed(self):
        if(self.Note == 0.0):
            return "~"
        elif(self.Note < 5.0):
            return "JA"
        return "NEIN"