"""(LEICHT)
Erstelle eine Klasse Person, die die Attribute name und age besitzt.
Erstelle eine Methode greet, die eine Begrüßung mit dem Namen der Person ausgibt.

"""

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hallo, mein Name ist {self.name}!")


lotta = Person("Lotta", 9)
lotta.greet()
