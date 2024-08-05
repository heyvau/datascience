"""(Leicht)
Erstelle eine Klasse Konto mit den Methoden 
withdraw (Abbuchen)
deposit (Einzahlen)
info (Liefert Kontostand in Euro)

Erstelle zwei Konto-Instanzen und überweise Geld von einem Konto auf das
andere. Ein Konto darf nicht überzogen werden (< 0 Euro). Einheiten werden im
Finanzbereich vorwiegend in Cent-Beträgen angegeben.

Beispiel:
konto_1 = Konto(initial=10_000, name="Bob")
konto_2 = Konto(initial=1200, name="Alice")
konto_2.info()
Auf dem Konto befinden sich zur Zeit 12.00 Euro

# Validierung der Eingabe
amount = konto_1.withdraw(amount="abc")
Dieser Vorgang ist nicht möglich!

# Überweisung von Konto 1 auf Konto 2
amount = konto_1.withdraw(amount=100)
konto_2.deposit(amount=amount)

Zusatz-Überlegungen
Was ist bei diesem Vorgehen problematisch? 

"""

class Konto:
    def __init__(self, initial, name):
        self.initial = initial
        self.name = name

    @property
    def initial(self):
        return self._initial

    @initial.setter
    def initial(self, initial):
        if initial < 0:
            raise ValueError("Ein Konto darf nicht überzogen werden")
        self._initial = initial


    def withdraw(self, amount):
        if isinstance(amount, int):
            self.initial -= amount
            return amount
        else:
            print("Dieser Vorgang ist nicht möglich!")


    def deposit(self, amount):
        if isinstance(amount, int):
            self.initial += amount
        else:
            print("Dieser Vorgang ist nicht möglich!")


    def info(self):
        print(f"Auf dem Konto von {self.name} befinden sich zur Zeit {(self.initial / 100):.2f} Euro")


def main():
    konto_1 = Konto(initial=10_000, name="Bob")
    konto_2 = Konto(initial=1200, name="Alice")
    konto_1.info()
    konto_2.info()

    # amount = konto_1.withdraw(amount="abc")
    try:
        amount = konto_1.withdraw(amount=100)
        konto_2.deposit(amount=amount)
        amount = konto_1.withdraw(amount=12_000)
        konto_2.deposit(amount=amount)
    except ValueError:
        print("Ein Konto wurde überzogen.")

    konto_1.info()
    konto_2.info()


if __name__ == "__main__":
    main()
