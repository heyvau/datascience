"""
Erstellen Sie eine Oberklasse Person
mit den Attributen name und age.
Erstellen Sie eine Unterklasse Student,
die von Person erbt und zusätzlich das Attribut student_id hat.

Implementieren Sie einen Konstruktor in jeder Klasse
und testen Sie die Klassen durch Erstellen von
Objekten (von Oberklasse und Unterklasse)

"""

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name: str, age: int, student_id: int) -> None:
        super().__init__(name, age)
        self.student_id = student_id


person = Person("Theo", 23)
print(f"Persons info: {person.name=}, {person.age=}")

student = Student("Heidi", 26, 3245364)
print(f"Students info: {student.name=}, {student.age=}, {student.student_id=}")
