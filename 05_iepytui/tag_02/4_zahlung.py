from abc import ABC, abstractmethod


class Zahlung(ABC):
    @abstractmethod
    def starte_zahlung(self, betrag: float):
        pass

    @abstractmethod
    def prüfe_zahlung(self):
        pass


class Kreditkartenzahlung(Zahlung):
    def starte_zahlung(self, betrag: float) -> str:
        return f"{self.__class__.__name__} von {betrag}."

    def prüfe_zahlung(self):
        return f"Überprüfung von {self.__class__.__name__}."


class PayPalZahlung(Zahlung):
    def starte_zahlung(self, betrag: float) -> str:
        return f"{self.__class__.__name__} von {betrag} Euro."

    def prüfe_zahlung(self):
        return f"Überprüfung von {self.__class__.__name__}."


kkz = Kreditkartenzahlung()
print(kkz.starte_zahlung(100.59))
print(kkz.prüfe_zahlung())

ppz = PayPalZahlung()
print(ppz.starte_zahlung(143.10))
print(ppz.prüfe_zahlung())
