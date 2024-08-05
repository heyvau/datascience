"""(LEICHT)
Company-Manager
Es soll eine Verwaltungssoftware erstellt werden, um Firmen und deren
Angestellte zu verwalten. Ein Angestellter kann immer nur in einer Firma
arbeiten, in jeder Firma arbeiten aber mehrere Angestellte.

Lege zwei Klassen an: Company und Employees.
Zeichne die Klassen-Diagramme, überlege die Assoziation (Aggregat oder
Komposition). Setze die Klasse zueinander in Beziehung.


bmw = Company(name="BMW")
angestellter_1 = Employee(first_name="Bobby", last_name="Fisher")

"""

# wenn wir Instanz von Employee löschen, eine Referenz wird weiter in der Liste employees behaltet.
# keine Garantie, dass ein Employee wird nicht in mehreren Companies arbeiten

from __future__ import annotations


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []


    def __repr__(self) -> str:
        return f"Company {self.name}"

    
    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            raise TypeError("argument type: Employee")
        self.employees.append(employee)


class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def __repr__(self) -> str:
        return f"Employee {self.first_name} {self.last_name}"


if __name__ == "__main__":

    bmw = Company(name="BMW")

    employees = [
        Employee(first_name="Bobby", last_name="Fisher"),
        Employee(first_name="Alice", last_name="Smith"),
        Employee(first_name="Tom", last_name="Jones")
    ]

    for emp in employees:  
        bmw.add_employee(emp)

    print(bmw.employees)

