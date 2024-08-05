"""
Aufgabe SEQUENCE READER

Der Sequence reader öffnet zwei Sequence-Dateien, die mit dem
Sequence-Generator erstellt wurden und vergleicht sie. (Falls die Datei im Pickle-Format vorliegt,
muss entpickelt werden.)

0. User gibt über Input die Namen zweier Sequenz-Dateien an. Existieren
diese Dateien am gesuchten Ort nicht, wird der User gewarnt, das Programm bricht ab.

1. Prüfe, ob die Sequenzen die gleiche Länge haben. Ist das nicht der
Fall, soll das Programm nur ausgeben, dass die Sequenzen nicht gleich
lang sind.

2. Sind die Sequenzen gleich lang, zähle die Anzahl der Matches
an allen Positionen mit Hilfe einer Schleife und eines Vergleichs der
Zeichen an der aktuellen Position.

3. Berechne aus der Anzahl der Matches und der Länge der Sequen-
zen die prozentuale Sequenzidentität.

Vergleich zweier Sequenzen (strings)

AAA
AAB
**-

ident count: 2
identity: 66.6 %

"""

from pathlib import Path
import pickle
import os

BASE_DIR = Path(__file__).resolve().parent


def get_sequence(sequence_name: str) -> tuple:
    with open(BASE_DIR / sequence_name, mode="rb") as pf:
        data = pickle.load(pf)
    return data


def user_input():
    first_name = input("Name der ersten Sequenz: ")
    second_name = input("Name der zweiten Sequenz: ")

    first_path = BASE_DIR / first_name
    second_path = BASE_DIR / second_name

    if not os.path.isfile(first_path):
        print(f"Die Datei '{first_name}' existiert nicht.")
        exit(-1)

    elif not os.path.isfile(second_path):
        print(f"Die Datei '{second_name}' existiert nicht.")
        exit(-1)

    return first_name, second_name


def sequence_compare(first_seq: str, second_seq: str) -> str:
    if len(first_seq) != len(second_seq):
        print("Die Sequenzen sind nicht gleich lang")
        exit()

    return "".join([
        ("*" if x == y else "-") 
        for x, y in zip(first_seq, second_seq)
    ])


def get_compare_result(s: str):    # Strenchen - gleich
    ident_count = s.count("*")
    ident_percent = ident_count * 100 / len(s)
    print(f"Identität: {ident_count}")
    print(f"Anzahl der Matches: {ident_percent:2.2f}")


def main():
    first_seq_name, second_seq_name = user_input()

    first_seq = get_sequence(first_seq_name)
    second_seq = get_sequence(second_seq_name)

    print("Die erste Sequenz:", first_seq)
    print("Die zweite Sequenz:", second_seq)

    comp_res_str = sequence_compare(first_seq, second_seq)

    print("Vergleich zweier Sequenzen:\n", comp_res_str)

    get_compare_result(comp_res_str)

if __name__ == "__main__":
    main()
