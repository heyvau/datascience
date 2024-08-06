from abc import ABC, abstractmethod


class Fahrzeug(ABC):
    @abstractmethod
    def starte_motor(self):
        pass

    def stoppe_motor(self) -> str:
        return "Der Motor wurde gestoppt"


class Auto(Fahrzeug):
    def starte_motor(self) -> str:
        return "Der Motor wurde gestartet"


auto = Auto()
print(auto.starte_motor())
print(auto.stoppe_motor())