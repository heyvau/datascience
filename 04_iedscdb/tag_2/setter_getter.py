"""
Vervollständige die Klasse Produkt und lege die entsprechenden Properties an. (MITTEL)

# Es gelten folgende Constraints (Regeln):
- Der Name muss mindestens drei Zeichen lang sein
- Der Preis darf nicht negativ sein und muss eine Zahl sein
- Die Verfügbarkeit muss den Zustand "in stock" oder "out of stock" haben.
- Im Fehlerfall raise ValueError.

Implementiere auch __str__ und __repr__.

Teste mit folgenden Produkten:
products = [
    ("Maggi", 23.2, "in stock"),
    ("Snickers", 4, "out of stock"),
    ("Petersilie", 1.9, "stock"),  # muss scheitern
    ("Gouda Käse", -12.50, "out of stock"), # muss scheitern
    ("Za", 23.2, "in stock"),  # muss scheitern.
]
Nutze zum testen einen Loop und try-except
"""

class Produkt:
    def __init__(self, name, preis, verfuegbarkeit):
        # Hier müssen die Instanzvariablen initialisiert werden
        self.name = name
        self.preis = preis
        self.verfuegbarkeit = verfuegbarkeit


    def __str__(self):
        return self.name

    
    def __repr__(self):
        return f"Produkt({self.name!r}, {self.preis!r}, {self.verfuegbarkeit!r})"  


    @property
    def name(self):
        # Getter-Methode für name
        return self._name


    @property
    def preis(self):
        # Getter-Methode für preis
        return self._preis
    
    @property
    def verfuegbarkeit(self):
        # Getter-Methode für verfuegbarkeit
        return self._verfuegbarkeit


    @name.setter
    def name(self, name):
        # Setter-Methode für name
        if len(name) < 3:
            raise ValueError("Die Angabe ist ungültig.")

        self._name = name


    @preis.setter
    def preis(self, preis):
        # Setter-Methode für preis
        if not (isinstance(preis, (int, float)) and preis > 0):             # thnx lazy evaluation
            raise ValueError("Die Angabe ist ungültig.")

        self._preis = preis


    @verfuegbarkeit.setter
    def verfuegbarkeit(self, verfuegbarkeit):
        # Setter-Methode für verfuegbarkeit
        if not verfuegbarkeit in ["in stock", "out of stock"]:
            raise ValueError("Die Angabe ist ungültig.")

        self._verfuegbarkeit = verfuegbarkeit
   

if __name__ == "__main__":

    products = [
        ("Maggi", 23.2, "in stock"),
        ("Snickers", 4, "out of stock"),
        ("Petersilie", 1.9, "stock"),  # muss scheitern
        ("Gouda Käse", -12.50, "out of stock"), # muss scheitern
        ("Za", 23.2, "in stock"),  # muss scheitern.
    ]

    for product in products:
        try:
            Produkt(*product)
        except ValueError:
            print(f"Angabe von {product} ist ungültig!")
        else:
            print(f"Instanz von {product} wurde erfolgreich erstellt.")
