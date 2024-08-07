from abc import ABC, abstractmethod
from math import pi


class Form(ABC):
    @abstractmethod
    def flaeche(self):
        pass


class Kreis(Form):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def flaeche(self):
        return round(pi * self.radius ** 2, 2)


kreis = Kreis(5)
print(kreis.flaeche())
