"""
Wetterdaten

Gegeben ist Datei wetterdaten.txt, die für jede Kalenderwoche Temperaturdaten enthält.
Der erste Wert in jeder Zeile ist die Kalenderwoche, zb. 12.
Durch einen Doppelpunkt ist er abgetrennt von den Tageshöchstwerten.

Beispiel für die Kalenderwoche 12 von Montag bis Sonntag:
12: mo34 tue33 wed22 thu 34 fri33 sat33 sun29

Jeder Tag hat ein Kürzel, zb. mo für Monday, tue für Dienstag,
gefolgt von einem Wert, der den Tageshöchstwert definiert

mo34 = Montag 34 Grad
tue33 = Dienstag 33 Grad

Der Wert für die Temperatur ist immer zweistellig,
zb. 34 für 34 Grad, 09 für 9 Grad, 00 für 0 Grad, und immer positiv.

In der Datei sind Fehler enthalten: an manchen Tagen wird die Zahl nicht direkt an das Kürzel gesetzt,
sondern durch ein Leerzeichen davon getrennt. Das passiert sporadisch. 

thu 34 = Donnerstag 34 Grad
tue 19 = Dienstag 19 Grad

Aufgabe:

1) Die Datei soll eingelesen und geparst werden.
Aus den bereinigten Daten soll ein Dictionary erstellt werden.
Schreibe dafür die nötigen Funktionen.
Die Kalenderwoche (als String) dient als Key des neuen Dictionaries,
eine Liste mit den numerischen Temperaturen für die Woche als value:

d = {
    '12': [34, 33, 22, 34, 33, 33, 29],
    '13': [22, 33, 32, 32, 23, 33, 28],
    [..]
}
Nutze Typehints, List-Comprehensions, doc-String und String-Funktionen (siehe übersicht String-Funktionen)

"""
from pathlib import Path
from string import ascii_lowercase
from collections.abc import Generator
from pprint import pprint

DATA_FILE = 'wetterdaten.txt'
BASE_DIR = Path(__file__).resolve().parent


def get_data_from_file(data_file: str) -> Generator[str, None, None]:       # [YieldType, SendType, ReturnType]
    """
    Die Funktion-Generator liest die Datei und generiert die Zeilen.
    Wenn die Datei nicht existiert, wird das Program mit einer Benahrichtung beendet.
    """

    try:
        with open(BASE_DIR / data_file, "r", encoding="utf-8") as f:
            for line in f:
                yield line.strip()

    except FileNotFoundError:
        print(f"Leider konnte die datei '{data_file}' nicht gefunden werden.")
        exit(-1)


def get_temperatures_list(week_temperatures: str) -> list[int]:
    """
    Die Funktion parst angegebenen String mit Temperaturdaten für eine Woche und
    gibt eine Liste zurück, die reine int-Werte enthaltet.
    """

    str_temperatures = (
        item.strip(" " + ascii_lowercase)
        for item in week_temperatures.split()
    )

    return [int(item) for item in str_temperatures if item]


def get_clean_data(data_gen: Generator) -> dict:
    """
    Die Funktion erstellt ein Dictionary aus den angegebenen Daten,
    wo die Kalenderwoche als Schlüssel und
    eine Liste mit den numerischen Temperaturen für die Woche als Wert dient.
    """

    raw_data = (
        line.split(":")
        for line in data_gen
    )

    return {
        line[0]: get_temperatures_list(line[1])
        for line in raw_data
    }


def main():
    data_gen = get_data_from_file(DATA_FILE)

    pprint(get_clean_data(data_gen))


if __name__ == "__main__":
    main()
