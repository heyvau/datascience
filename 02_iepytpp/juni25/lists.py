# Aufgaben:

# Definieren Sie die folgende Liste:

num_list = [10, -90, 1001, 43, -800]


# 1. Messen Sie die Länge der Liste mit der Funktion len() und geben Sie diese aus.

num_list_length = len(num_list)
print(f"Die Länge der Liste {num_list}: {num_list_length}")


# 2. Geben Sie die einzelnen Werte von num_list aus, indem Sie den zugehörigen Index
# referenzieren.

for _ in range(num_list_length):
    print(f"Index: {_}, Wert: {num_list[_]}")


# 3. Erstellen Sie zunächst eine leere Liste mit dem Namen: num_list_geordnet und ermitteln
# Sie mit der Funktion type(), ob es sich auch wirklich um eine Liste handelt.

num_list_geordnet = list()
print(f"Type: {type(num_list_geordnet)}")

if isinstance(num_list_geordnet, list):
    print("Ich bin eine Liste, ich wusste es!")
else:
    print("Was bin ich dann?")


# 4. Fügen Sie nun, zu der in 3. erstellten Liste die Werte von num_list nach und nach mit
# der Methode append() so hinzu, dass die Liste num_list_geordnet die Werte von num_list in
# aufsteigender Reihenfolge enthält.

# kurz
# num_list_geordnet = sorted(num_list).copy()

for _ in sorted(num_list):
    num_list_geordnet.append(_)

print(num_list_geordnet)


# 5. Erstellen Sie eine weitere Liste num_list_geordnet_2, wo Sie bei Erstellung der Liste direkt
# die, nach der Reihenfolge, geordneten Indizes von num_list zuweisen.
# (Hab ich die Aufgabe richtig verstanden?)

num_list_geordnet_2 = [None] * num_list_length

for i in range(num_list_length):
    num_list_geordnet_2[i] = sorted(num_list)[i]

print(num_list_geordnet_2)
