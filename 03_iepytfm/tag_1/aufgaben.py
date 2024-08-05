"""
Implementiere die folgenden Funktionen.

Hinweis:
Führe print nicht in einer Funktion aus, es sei denn, es ist explizit
gewünscht.
--------------------------------------------------------------------
Die Ausgabe bezieht sich immer auf die Rückgabewerte der Funktion!!
--------------------------------------------------------------------
z.B.
def fn():
    return 1

result = fn()  # fn() aufrufen und Rückgabewert in result speichern
print(result) # den Rückgabewert von fn printen
"""

"""
0. Identitätsfunktion (LEICHT)
Schreibe eine Funktion identity, die einen Paramter hat und diesen Wert
unverändert zurückgibt.

value = identity(42)
print(value)
42
"""


def identity(x):
    return x

value = identity(42)
print(value)


"""
0.b Aufruf der Funktion für eine Liste  (MITTEL)
n = 10
Führe die Funktion identity für die range(n) aus und speichere das Ergebnis in
einer Liste, zum Beispiel via List-Comprehension.

"""


def list_identity(n):
    return [x for x in range(n)]

n = 10
res_liste = list_identity(n)
print(res_liste)


"""
1. Vokale zählen (MITTEL)
Schreibe eine Funktion count_vowels() die einen String als Parameter erwartet,
und alle Vokale  in diesem String zählt. Der Rückgabewert der Funktion ist die
Anzahl der Vokale (int). Als Vokale zählen im deutschen: aeiouüäö
Beachte Groß- und Kleinschreibung! Auge hat 3 Vokale
"""


VOKALE = "aeiouüäö"

def count_vowels(s):
    counter = 0
    for ch in s:
        if ch.lower() in VOKALE:
            counter += 1

    return counter

number_of_vowels = count_vowels("teleport")
print(number_of_vowels)

number_of_vowels = count_vowels("Ööll")
print(number_of_vowels)


"""
3. Liste filtern (MITTEL)
Schreibe eine Funktion filter_input(), die eine Liste A entgegennimmt und
anhand einer weiteren Liste B mit erlaubten Werten prüft, ob diese Werte
zulässig sind. Rückgabewert der Funktion ist eine Liste mit Werten, die
mithilfe B geprüft worden ist.
"""


def filter_input(A, B):
    res_liste = []
    for i in A:
        if i in B:
            res_liste.append(i)

    return res_liste

input_filtered = filter_input([1, 3, 4, 5, 3], [3, 4])
print(input_filtered)

input_filtered = filter_input([1, 3, 4, 5, 3], [])
print(input_filtered)

input_filtered = filter_input(["gold", "gelb", "gelb", "rot", "gelb"], ["gelb", "rot"])
print(input_filtered)


"""
4. Rückwärts (SCHWER)
Schreibe eine Funktion reverse_cutter(), die einen String entgegennimmt, diesen
zu Kleinbuchstaben transformiert, den ersten und letzten Index abschneidet und
das Ergebnis umgedreht zurückgibt. Ein Input kleiner gleich Länge zwei gibt
einen leeren String zurück.
"""


def reverse_cutter(s):
    if len(s) < 3:
        return ""
    return s[-2:0:-1].lower()
    
rev_s = reverse_cutter("Petersburg")
print(rev_s)


"""
5. Max (MITTEL)
Implementiere die Funktion max. Diese soll aus einer gegebenen Liste von
Integerwerten den größten Wert zurückgeben. Nutze dazu nicht die Built-In
Funktion max oder max aus dem Numpy-Modul! Die Funktion soll None zurückgeben,
wenn eine leere Liste übergeben wurde.
"""


def max(l):
    if not l:
        return None
    max_i = l[0]
    for i in l:
        if i > max_i:
            max_i = i
    return max_i

values = [3, 2, 4]
x_max = max(values)
print(x_max)

values = []
x_max = max(values)
print(x_max)


"""
6. Median (SCHWER)
Implementiere die Funktion median(), die eine Liste von Integerwerten
entgegennimmt und den Median berechnet. Prüfe die Funktion mit verschiedenen
Input-Werten! Nicht die Funktion median aus dem Numpy Modul o.ä. nutzen.
Ergebnis kann hier geprüft werden:
http://www.alcula.com/calculators/statistics/median/
"""


def median(l):
    if not l:
        return None

    l = sorted(l)

    if len(l) % 2:
        median = l[len(l) // 2]
    else:
        median = (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2

    return median

x_median = median([1, 50, 65, 34, 0, 6, 4, 2, 3])
print("Median:", x_median)


""" (LEICHT)
7. Schwellenwertfunktion (Heaviside, Hard Limit)
Eine Funktion, die häufig im Zusammenhang mit neuronalen Netzen
genutzt wird, ist die Heaviside funktion.
Sie gibt 1 zurück, wenn der Eingangswert größergleich 0 ist, ansonsten,
gibt sie 0 zurück.

Hintergrundwissen:
https://de.wikipedia.org/wiki/Heaviside-Funktion
"""


def heaviside(x):
    return (0 if x < 0 else 1)

x = -1
print(heaviside(x))


"""
8. Rectifier (RELU) (MITTEL)
im DeepLearning häufig genutze Funktion, die als Positivteil ihres Arguments
definiert ist.

Hintergrundwissen:
https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html

f(v) = max(0, v)

Führe die Funktion von der Range -10 bis 10 aus, zum Beispiel via einer
List-Comprehension.
"""


def relu(x):
        return (x if x > 0 else 0)

result = [relu(x) for x in range(-10, 10)]
print(result)


"""
9. Sigmoid (Schwer)
in neuronalen Netzen genutze Aktivierungsfunktion
https://de.wikipedia.org/wiki/Sigmoidfunktion
"""


from math import exp

def sigmoid(x):
    return 1 / (1 + exp(-x))


result = sigmoid(-5)
print(result)
result = sigmoid(0)
print(result)
result = sigmoid(5)
print(result)

