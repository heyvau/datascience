"""
Erstellen Sie eine Oberklasse Buch
mit den Instanzattributen titel und autor.

Erstellen Sie eine Unterklasse Ebook,
die von Buch erbt und zusätzlich
das Instanzattribute dateigroesse hat.

Verwenden Sie super(), um den Konstruktor der Oberklasse
im Konstruktor der Unterklasse aufzurufen.

Implementieren Sie in beide Klassen die Methode get_info(),
die die Informationen über das Buch oder Ebook zurückgibt.

Z.B.
Buch: 1984 von George Orwell
Ebook: Digital Fortress von Dan Brown, Dateigröße: 2MB

Testen Sie die Klassen durch Erstellen von Instanzen und Aufrufe der Methode get_info().

"""

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def get_info(self) -> None:
        print(f"\n{self.__class__.__name__} Info\nTitle: {self.title} von {self.author}")


class Ebook(Book):
    def __init__(self, title: str, author: str, file_size: float) -> None:
        super().__init__(title, author)
        self.file_size = file_size

    def get_info(self) -> None:
        super().get_info()
        print(f"Size of file: {self.file_size}MB\n")


book = Book("1984", "George Orwell")
book.get_info()

ebook = Ebook("Digital Fortress", "Dan Brown", 2)
ebook.get_info()