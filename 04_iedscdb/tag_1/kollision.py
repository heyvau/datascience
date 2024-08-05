""" (MITTEL)
Erstelle eine Klasse Kreis mit der Eigenschaft radius, x und y Koordinate im
kart. Koordinatensystem.
Erstelle zwei Instanzen dieser Klasse auf Basis einer Usereingabe (input).

Prüfe, ob sich die Kreise schneiden / überlagern oder nicht.

User-Beispiel:

Bitte gebe den Radius, X und Y Koordinate des ersten Kreises ein:
10, 23, 14 

Bitte gebe den Radius, X und Y Koordinate des zweiten Kreises ein:
4, 12, 55 

Die Kreise schneiden sich nicht.

Wollen Sie eine weitere Kollision überprüfen? J/N 


-------
Im Entwurf dieser Aufgabe seid ihr vollkommen frei. Wir gehen von legalem Input
aus.
...

Code-Beispiel


class Circle(...):
    ...

def main():
    # user input Kreis 1
    r = userinput("r")
    x = userinput("x")
    y = userinput("y")
    circle_1 = Circle(radius=r, x=x, y=y)

    # user input Kreis 2
    r = userinput("r")
    x = userinput("x")
    y = userinput("y")
    circle_2 = Circle(radius=r, x=x, y=y)

    # Prüfe, ob sich Kreise schneiden / überlagern ...

    # Weitere Prüfung? Y/N?

"""

import math


class Circle:
    def __init__(self, radius: float, x: float, y: float):
        self.radius = radius
        self.x = x
        self.y = y


def check_intersection(circle_1: Circle, circle_2: Circle) -> bool:
    """
    Falls angegebene Kreise sich scheiden,
    wird True zurueckgegeben, ansonsten False
    """
    # euclidische Distanz zwischen den Kreismitten
    e_dist = math.dist(
        [circle_1.x, circle_1.y],
        [circle_2.x, circle_2.y]
    )

    # die Kreise schneiden sich,
    # wenn die Summe von Radiusen groesser,
    # als die euclidische Distanz ist

    return (circle_1.radius + circle_2.radius) > e_dist



def main():

    while True:

        ui_circle_1 = input("\nBitte gebe den Radius, X und Y Koordinate des ersten Kreises ein: ")
        data_circle_1 = [float(i) for i in ui_circle_1.split()]
        circle_1 = Circle(*data_circle_1)

        ui_circle_2 = input("\nBitte gebe den Radius, X und Y Koordinate des zweiten Kreises ein: ")
        data_circle_2 = [float(i) for i in ui_circle_2.split()]
        circle_2 = Circle(*data_circle_2)

        if check_intersection(circle_1, circle_2):
            print("\nDie Kreise schneiden sich.")
        else:
            print("\nDie Kreise schneiden sich nicht.")

        while True:
            ui = input("\nWeitere Prüfung? Y/N? ")
            
            match ui:
                case "y" | "Y":
                    break
                case "N" | "n":
                    print("\nBis bald!")
                    exit()
                case _:
                    print("\nVersuche nochmal.")


if __name__ == "__main__":
    main()     

