""" (MITTEL)
Erstelle eine einfache Todo-Liste.

die Klasse TodoListe verwaltet Todos (Strings).
Dazu wird ein User-Interface in einem While-Loop benötigt.

Diese drei Kommandos muss das Programm mindestens unterstützen:
Hinzufügen von einem todo (add)
Löschen von einem todo (del)
Anzeigen aller Todos (show)

Zusatzaufgabe (schwer)
Die einzelnen Todos können auch als Klasse Todo angelegt werden.
Das hat den Vorteil, dass ein Todo auch weitere Eigenschaften haben kann,
zb. Uhrzeit oder Notiz.
"""
import datetime


PRIORITY = {
    1: "low",
    2: "neutral",
    3: "high"
}


class Todo:
    def __init__(self, title: str, description="", priority=1):
        self.title = title
        self.description = description
        self.priority = priority
        self.date = datetime.datetime.now().strftime('%H:%M, %d-%m-%Y')


    def print_info(self):
        
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Priority: {PRIORITY.get(self.priority)}")
        print(f"Date: {self.date}")
        print("\n")


class TodoList:
    def __init__(self, owner, todo_list):
        self.owner = owner
        if todo_list:
            self.todos = todo_list
        else:
            self.todos = []


    def add_todo(self):
        titel = input("Titel: ")
        description = input("Description: ")
        priority = int(input("Priority (1-low, 2-neutral, 3-high): "))

        self.todos.append(Todo(titel, description, priority))


    def del_todo(self):
        title_to_del = input("Titel zu löschen: ")

        for todo in self.todos:
            if  todo.title == title_to_del:
                self.todos.remove(todo)
                print(f"\nTodo '{title_to_del}' wurde erfolgreich gelöscht")
                break
        else:
            print(f"\nTodo '{title_to_del}' konnte nicht gefunden werden.")


    def show_todos(self):
        print(f"\n********** TodoListe von {self.owner} **********\n")

        if self.todos:
            for todo in self.todos:
                todo.print_info()
        else:
            print("Da gibt's nichts zu zeigen.\n")


    def clear(self):
        self.todos.clear()
        print("Ihre TodoListe ist leer.\n")


todos_list = [
    Todo("Zähne putzen", description="Gestern hab es vergessen", priority=3),
    Todo("Hände waschen", priority=2),
    Todo("Schleife binden"),
    Todo("Treppen steigen"),
    Todo("Päckchen packen"),
    Todo("Bücher lesen", description="Dabei versuchen nicht einzuschlafen"),        
    Todo("Briefe schreiben", priority=3),
    Todo("Kuchen backen", description="Mit Erdbeeren"),
    Todo("Kaffee kochen")
]


def main():
    teds_todos = TodoList("Ted", todos_list)

    while True:

        print("\n")
        print("********** Menu **********")
        print("\n")
        print("0 - Schließen")
        print("1 - Anzeigen aller Todos")
        print("2 - Hinzufügen von einem Todo")
        print("3 - Löschen von einem Todo")
        print("4 - Leeren von TodoListe")
        print("\n")
        
        ui = int(input(">> "))

        match ui:
            case 0:
                exit()
            case 1:
                teds_todos.show_todos()
            case 2:
                teds_todos.add_todo()
            case 3:
                teds_todos.del_todo()
            case 4:
                teds_todos.clear()

        input("ENTER um fortzufahren...")


if __name__ == "__main__":
    main()