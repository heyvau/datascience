# 2. Schreibe eine Funktion big_if_red(), die einen String entgegennimmt,
# und diesen String in Großbuchstaben umwandelt, wenn er "Red" ist, d.h. wenn
# genau diese Zeichenfolge übergeben wurde, unabhängig von Groß- und
# Kleinschreibung


def big_if_red(word):
    return (word.upper() if word.upper() == "RED" else word)


x = big_if_red("rED")
print(x)
"RED"

x = big_if_red("ReD")
print(x)
"RED"

x = big_if_red("ReDo")
print(x)
"ReDo"


# Gegeben ist die quadratische Gleichung y = 2x^2
# Erstelle dazu eine Python-Funktion f mit einem Parameter x, der für ein x den
# y-Wert errechnet


def f(x):
    return 2 * pow(x, 2)


y = f(5)                    # 50
print(y)
y = f(2)                    # 8
print(y)


# 3.  Schreibe eine Funktion swap(), die zwei Parameter besitzt und
# diese vertauscht zurückgibt.


def swap(a, b):
    return (b, a)


a, b = swap(1, 2)
print(a, b)                 # 2, 1


# 4.  Lese die Temperaturen aus. Schreibe dazu eine Funktion get_temperature(),
# die den Ort und das temp-Dictionary entgegennimmt, und die Temperaturliste
# zurückgibt. Fehlt der Eintrag, gibt get_temperature() None zurück.


def get_temperatures(ort, temp_dict):
    return temp_dict.get(ort)


temperatures = {
    "munich": [32, 22, 33, 11, 44, 12, 25, 15],
    "dresden": [12, 22, 23, 11, 22 , 12, 22, 8],
    "berlin": [33, 42, 13, 11, 24, 22, 20, 10]
}

print(get_temperatures('berlin', temperatures))             # ergibt [33, 42, 13, 11, 24, 22, 20, 10]
print(get_temperatures('bielefeld', temperatures))          # ergibt None


# 4.1. Als Zusatz kann die Durchschnittstemperatur ausgegeben werden. Dies darf
# aber auf keinen Fall in der Funktion get_temperatures passieren,
# sondern muss in einer anderen Funktion errechnet werden, z.b. calculate_average.


def calculate_average(ort, temp_dict):
    ort_temps = get_temperatures(ort, temp_dict)
    if ort_temps:
        return sum(ort_temps) / len(ort_temps)


print(calculate_average('berlin', temperatures))
print(calculate_average('bielefeld', temperatures))


# 5. Multi Replace
# Schreibe eine Funktion Multi-Replace, die drei
# Parameter entgegennimmt:
# to_be_replaced = Liste mit zu ersetzenden Strings
# replacements = Liste mit den Ersetzungen
# s = ein String

# Falls die Sequenzen mit den Ersetzungen
# nicht die gleiche Länge haben sollten,
# wird der Original-String zurückgegeben!


def multi_replace(to_be_replaced, replacements, s):

    if len(to_be_replaced) == len(replacements):

        for w1, w2 in zip(to_be_replaced, replacements):
            s = s.replace(w1, w2)
    return s


to_be_replaced = ["Affe", "lebt", "Eis"]
replacements = ["Maki", "döst", "Schokolade"]
s = "Ein Affe lebt auf einem Baum und isst Eis"

print(multi_replace(to_be_replaced, replacements, s))
# Ein Maki döst auf einem Baum und isst Schokolade

to_be_replaced = ["rot"]
replacements = ["blau", "grün"]
s = "Ein roter Hut"

print(multi_replace(to_be_replaced, replacements, s))
# Ein  roter Hut


# 6. Schreibe eine Funktion replace_umlauts, die einen String
# entgegennimmt und alle deutsche Umlaute unter Berücksichtung
# von Groß- und Kleinschreibung ersetzt. Der Rückgabewert
# ist der String mit den Ersetzungen.

# Österü => Oesterue


def replace_umlauts(s):
    umlaute = {
        "ö": "oe",
        "ä": "ae",
        "ü": "ue",
        "Ö": "Oe",
        "Ä": "Ae",
        "Ü": "Ue",
    }
    for ch in umlaute:
        s = s.replace(ch, umlaute[ch])

    return s


s = "Österü"
print(replace_umlauts(s))


# 7.  Char-Counter. Schreibe eine Funktion char_counter(),
# die einen String entgegennimmt und die einzelnen Zeichen des Strings zählt.
# Das Ergebnis soll ein Dictionary mit den Vorkommen der Zeichen sein.
# Groß- und Kleinschreibung soll ignoriert werden.
# Deutsche Umlaute werden umgeschrieben.


def char_counter(s):
    d = {}
    s = replace_umlauts(s).lower()
    for ch in s:
        d[ch] = s.count(ch)
    return d


result = char_counter("Überlingen")
print(result)
# {'u': 1, 'e': 3, 'b': 1, 'r': 1, 'l': 1, 'i': 1, 'n': 2, 'g': 1}
