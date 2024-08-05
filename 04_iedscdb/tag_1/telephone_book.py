"""
(SCHWER)
Es sollen Klassen für eine Telefonbuch-App modelliert werden. 
Wir benötigen zwei Klassen:
- Entry: ein Telefonbuch-Eintrag 
- TelephoneBook: das Telefonbuch, welches Telefonbuch-Einträge verwaltet.

Modelliere die Klassen und erstelle die dazugehörigen Instanzen.
Hinweis: die Telefonnummern müssen numerisch sein, das ist die einzige
Anforderung.
Es ist nicht nötig, ein User-Interface mit input oder ähnlichem zu entwickeln.

Anbei einige Nutzungsbeispiele:

book = TelephoneBook(name="privates Telefonbuch")

book.add(name="Bob", number="23423432")
book.add(name="Alice", number="23423432", birthday="23.11.1987")
book.add(name="Bob", number="11123423432")
Es befindet sich schon ein Nutzer namens Bob im System!

book.add(name="Trudy", number="AAA23423432")
Diese Telefonnummer ist nicht gültig.

book.list_entries()
Bob: 232242424
Alice: 232423211

book.list_entries(filter_name="B")
Bob: 232242424

book.delete(name="Bob")
Nutzer Bob wurde gelöscht

book.delete(name="Bob")
es konnte kein Nutzer Bob gefunden werden
"""


class Entry:
    def __init__(self, name, tel_number, birthday):
        self.name = name
        self.tel_number = tel_number
        self.birthday = birthday


class TelephoneBook:
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.__entries = []


    def add(self, name, tel_number, birthday=None):
        for entry in self.__entries:

            if entry.name == name:
                print(f"Es befindet sich schon ein Nutzer namens {name} im System!")
                break

            elif not tel_number.isdigit():
                print("Diese Telefonnummer ist nicht gültig.")
                break
            
        else:
            self.__entries.append(Entry(name, tel_number, birthday))


    def delete(self, name_to_del):
        for entry in self.__entries:

            if entry.name == name_to_del:
                self.__entries.remove(entry)
                print(f"Der Nutzer namens {name_to_del} wurde erfolgreich gelöscht.")
                break
            
        else:
            print(f"Der Nutzer namens {name_to_del} konnte nicht gefunden werden.")


    def list_entries(self, filter_name=""):
        for entry in self.__entries:

            if entry.name.startswith(filter_name):
                print(f"{entry.name}: {entry.tel_number}")


def main():

    book = TelephoneBook(owner="Mimi", name="privates Telefonbuch")

    book.add(name="Bob", tel_number="23423432")
    book.add(name="Alice", tel_number="23423432", birthday="23.11.1987")
    book.add(name="Bob", tel_number="11123423432")
    # Es befindet sich schon ein Nutzer namens Bob im System!

    book.add(name="Trudy", tel_number="AAA23423432")
    # Diese Telefonnummer ist nicht gültig.

    book.list_entries()
    # Bob: 232242424
    # Alice: 232423211

    book.list_entries(filter_name="B")
    # Bob: 232242424

    book.delete(name_to_del="Bob")
    # Der Nutzer namens Bob wurde erfolgreich gelöscht.

    book.delete(name_to_del="Bob")
    # Der Nutzer namens Bob konnte nicht gefunden werden.
    

if __name__ == "__main__":
    main()
