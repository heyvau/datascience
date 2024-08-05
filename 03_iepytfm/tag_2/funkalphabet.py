# Gruppenaufgabe: Funkalphabet Übersetzer (schwer)

# Worte sollen in ein Funk-Alphabet übersetzt werden. zum Beipiel das deutsche
# Funkalphabet:
# Hans
# Heinrich – Anton – Nordpol - Samuel

# https://de.wikipedia.org/wiki/Buchstabiertafel
# https://en.wikipedia.org/wiki/NATO_phonetic_alphabet

# Natoformat
# Julia
# Juliett Uniform Lima India Alfa

# Aufgabe:
# Es soll ein Programm geschrieben werden,
# welches verschiedene Funk-Alphabete (deutsch, nato) einlesen kann.
# Der User kann während des Betriebs wählen,
# welches Funkalphabet er nutzen möchte.
# Die Alphabete liegen als txt-Dateien
# in folgendem Format vor:

# D Delta
# E Echo
# F Foxtrot
# [..]

# Nach Wahl des Funkalphabets kann der User Worte eingeben, die in
# das gewählte Alphabet übersetzt werden.

# Das Programm bzw. der Userinput läuft in einem while-Loop
# und terminiert erst bei Eingabe des Wortes _q bzw. _quit

# folgende Funktionen sollen implementiert werden:
# ------------------------------------------------

# def load_data_from_file(filename): => Daten aus der txt-Datei einlesen und
# als geeignete Datenstruktur, zb. Dictionary als Returnwert zur Verfügung
# stellen.

# def translate(word, alphabet) => ein Wort in Abhängigkeit des gewählten
# Alphabets (deutsch/nato/...) übersetzen und als String zurückgeben.
# Das alphabet könnte zum Beispiel ein Dict sein.

# def choose_alphabet() => ein Sub-Programm zum wählen eines Alphabetes.
# Rückgabewert ist das gewählte und geladene Alphabet (zum Beispiel als Dict.)

# def main() => das Hauptprogramm, von wo aus alles gestartet wird.

# Bitte beachten!
# Beispielhafter Ablauf:

# Welcome to the phonetic alphabet Translator
# Choose alphabet with _c or quit translator with _q
# Please choose an alphabet from list to proceed:
# D: Deutsches Funkalphabet
# N: Nato Funkalphabet
# Please choose Alphabet: D

# you have chosen: Deutsches Funkalphabet
# Enter: hans
# Heinrich Anton Nordpol Samuel
# Enter: _c
# Please choose an alphabet from list to proceed:
# D: Deutsches Funkalphabet
# N: Nato Funkalphabet
# Please choose Alphabet: N
# you have chosen: Nato Funkalphabet
# Enter: Julia
# Juliet Uniform Lima India Alfa
# Enter: _q
# Goodbye


from pathlib import Path


EXIT_WORDS = ["_q", "_quit"]
WORD_DELIMITER = " "


def load_data_from_file(filename):
    """
    Load data from file and build phonetic dict.
    """

    d = {}
    with open(f"{Path(__file__).parent}/alphabets/{filename}",
              "r", encoding="utf-8") as f:
        for line in f:
            value = line.split(" ")
            d[value[0]] = value[1].strip()
        
    return d


def translate(alphabet):
    """
    Translate word to phonetic alphabet. Skip missing letters.
    """
    word = input("Enter: ")
    
    l = [
        alphabet.get(ch)
        for ch in word.upper()
        if ch in alphabet]

    return WORD_DELIMITER.join(l)


def choose_alphabet():
    """
    User Interface Function to choose an alphabet via input.
    """

    print(
        "Please choose an alphabet from list to proceed: \
        \nD: Deutsches Funkalphabet \
        \nN: Nato Funkalphabet\n")
    
    ui = input("Please choose Alphabet: ")

    if ui == "D":
        print("You have chosen: Deutsches Funkalphabet")
        return load_data_from_file("deutsch.txt")

    elif ui == "N":
        print("You have chosen: Nato Funkalphabet")
        return load_data_from_file("nato.txt")


def get_translation():
    alphabet = choose_alphabet()
    return "Input is incorrect" if not alphabet else translate(alphabet)


def main():

    print("Welcome to the phonetic alphabet Translator!")

    while True:
        ui = input("\nChoose alphabet with _c or quit translator with _q or _quit.\n")
        
        if ui in EXIT_WORDS:
            print("Goodbye!")
            break

        elif ui == "_c":
            print(get_translation())

        else:
            print("Input is incorrect.")


main()
