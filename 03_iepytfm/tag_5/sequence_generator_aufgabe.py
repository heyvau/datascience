"""
Aufgabe SEQUENCE GENERATOR
Erzeugen Sie eine Sequenzvariable und schreiben Sie ihre Testsequen-
z in eine Datei, zb. als Pickle oder Text.
Die Sequenz soll zufällig erstellt werden.

Der User kann über input eingeben:
    die Länge der Sequence, die generiert werden soll (int)
    der Zeichenvorrat, der verwendet werden soll. Z.b. ABC. Werte sind unique.
    der Name der Sequence. Dieser Name ist der Filename der generierten Sequenz
    Die Datei hat keinen Dateisuffix


Beispiel:
Bitte Sequenz-Länge eingeben: 5
bitte den Zeichenvorrat eingeben: ABO
Name der Sequence: ABO5

Ergebnis: AABAO
die datei ABO5 enthält jetzt die Zeichenkette AABAO
"""

from pathlib import Path
import pickle
import random

# Das Verzeichnis, in dem das aktuelle Programm liegt
BASE_DIR = Path(__file__).resolve().parent


def generate_sequence(length: int, chars: str) -> str:
    return "".join(random.choices(chars, k=length))


def save_sequence(sequence_name: str, sequence: str) -> None:
    with open(BASE_DIR / sequence_name, mode="wb") as pf:
        pickle.dump(sequence, pf)


def get_user_input() -> tuple:
    """return user input:chars, length, name as tuple."""

    while True:
        length = input("Bitte Sequenz-Länge eingeben: ")

        if not length.isdigit():
            print("Nur Zahlen sind gültig.")
            continue

        while True:

            chars = input("Bitte den Zeichenvorrat eingeben: ")

            if len(chars) != len(set(chars)):
                print("Die Werte müssen unique sein.")
                continue

            break
        break

    name = input("Name der Sequence: ")

    return chars, int(length), name


def main():
    """
    Hauptprogramm:
    im Endlos-Loop:
        1. Userinput holen (oder Abbruch)
        2. Sequenz Generieren
        3. Sequenz speichern
    """

    user_data = get_user_input()
    chars, length, name = user_data

    seq = generate_sequence(length, chars)

    print(f"Ihre Sequenz '{seq}' wurde in die Datei '{name}' gespeichert.")

    save_sequence(name, seq)


if __name__ == "__main__":
    main()
