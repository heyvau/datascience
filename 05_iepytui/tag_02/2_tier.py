from abc import ABC, abstractmethod


class Tier(ABC):
    @abstractmethod
    def laut(self):
        pass

    @abstractmethod
    def bewegung(self):
        pass


class Hund(Tier):
    def laut(self) -> str:
        return "wau-wau"

    def bewegung(self) -> str:
        return "stampf-stampf"


charlie = Hund()
print(f"{charlie.__class__.__name__} macht {charlie.laut()} und {charlie.bewegung()}")