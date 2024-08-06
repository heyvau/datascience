"""
Erstellen Sie eine Oberklasse Mitarbeiter
mit einer Instanzmethode get_role() und dem Instanzattribut name.
Die Instanzmethode get_role() gibt die Nachricht
z.B.„Alex hat eine allgemeine Mitarbeiterrolle“ aus.

Erstellen Sie Unterklassen Manager und Entwickler,
die die Methode get_role() überschreiben,
um spezifische Nachrichten auszugeben,
die die jeweilige Rolle des Mitarbeiters beschreiben.

z.B. „Bob ist ein Manager, der die Teamarbeit überwacht.“
„Carol ist ein Entwickler, der Code schreibt und wartet.“

Testen Sie die Methodenüberschreibung durch Erstellen von Instanzen und Aufrufen der Methoden

"""

class Mitarbeiter:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_role(self) -> None:
        print(f"{self.name} hat eine allgemeine Mitarbeiterrolle.")


class Manager(Mitarbeiter):
    def get_role(self) -> None:
        print(f"{self.name} ist ein Manager, der die Teamarbeit überwacht.")


class Entwickler(Mitarbeiter):
    def get_role(self) -> None:
        print(f"{self.name} ist ein Entwickler, der Code schreibt und wartet.")


mitarbeiter  = Mitarbeiter("Frida")
mitarbeiter.get_role()

manager = Manager("Yulius")
manager.get_role()

entwickler = Entwickler("Petra")
entwickler.get_role()
