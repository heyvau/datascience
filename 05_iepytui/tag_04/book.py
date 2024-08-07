class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Titel: {self.title}\nAutor: {self.author}\nSeiten: {self.pages}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f"Buch '{self.title}' wurde erfolgreich gelöscht.")

b = Book("Lord of Rings", "J. R. R. Tolkien", 1216)
print(b)
print(len(b))
del b
print(b)