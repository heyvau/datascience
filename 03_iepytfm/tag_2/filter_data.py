# Lese die Daten aus log.txt und bereinige die Zahlen von allen anderen Zeichen.
# Leerzeichen lösche raus.

# Speichere die veränderten Daten in eine Datei log_clean.txt

# Nutze dazu folgenden vordefinierten Funktionen.
# Man kann davon ausgehen, dass die log.txt 1000 Einträge nicht übersteigt, der
# Content der Datei kann also problemlos in den RAM gelesen werden.

from pathlib import Path


def read_data(filename):
    """Einlesen der Daten.

    Datei öffnen und zeilenweise einlesen
    Es sollen die Roh-Daten als Liste von Strings zurückgegeben werden.
    Rückgabewert ist also eine Liste (von Strings)
    """
    with open(Path(__file__).parent / filename, "r", encoding="utf-8") as f:
        return [line for line in f if line.strip()]


def int_filter(s):
    res = ""
    for ch in s:
        if ch.isdecimal():
            res += ch
        else:
            break
    return res


def filter_data(word_list):
    """Filtere die Daten und befreie sie von unzulässigen Zeichen.

    Die Funktion bekommt eine word_list übergeben (Liste von Strings)
    Die Zeilen sollen am Ende jeweils nur eine Ganzzahl als String enthalten.
    Leerzeilen sollen entfernt werden.  Ein Konvertieren nach int ist
    nicht notwendig.

    Rückgabewert ist eine Liste von Strings:
    ["24343", "34341", "3422"]

    """
    return [int_filter(word) for word in word_list]


def write_data(filename, word_list):
    """Die sauberen Daten sollen zeilenweise in eine Datei geschrieben werden.
    hier soll ein Dateiname und eine Liste von Strings übergeben werden.
    Der Rückgabewert ist None
    """
    with open(Path(__file__).parent / filename, "w", encoding="utf-8") as f:
        for word in word_list:
            f.write(word + "\n")


def main():
    """Hauptprogramm. Führe die Reihenfolge wie folgt aus:
    - Daten einlesen (read_data) EXTRACT
    - Daten filtern / bereinigen (filter_data) TRANSFORM
    - Daten schreiben (write data) LOAD
    """
    raw_data = read_data("log.txt")
    print(raw_data, end="\n\n")

    clean_data = filter_data(raw_data)
    print(clean_data, end="\n\n")

    write_data("log_clean.txt", clean_data)


main()
