# Gegeben seien die folgenden 2 sets:

s1 = set({1, 2})
s2 = set({5, 6})


# 1. Messen Sie mit type(), ob es sich auch wirklich um sets handelt.

print(f"Typ von s1: {type(s1)}")
print(f"Typ von s2: {type(s2)}")


# 2. Berechnen Sie deren Schnittmenge mit der Funktion intersection(). Speichern
# Sie das Ergebnis dabei in einer neuen Variablen mit dem Namen s1_s2_int ab.
# Was enthält s1_s2_int?

s1_s2_int = s1.intersection(s2)
print(f"Schnittmenge von {s1} und {s2} ist: {s1_s2_int}")


# 3. Prüfen Sie mit isdisjoint() ob die beiden sets gemeinsame Werte haben.

if s1.isdisjoint(s2):
    print(f"Sets {s1} und {s2} haben keine gemeinsame Werte")
else:
    print(f"Sets {s1} und {s2} haben gemeinsame Werte")


# 4. Erweitern Sie s1 und s2 so, dass beide die Werte 3 und 4 hinzubekommen.
# Nutzen Sie hierzu die Methode add().

s1.add(3)
s1.add(4)
s2.update([3, 4])

print("-----------------------------------------------")

# 5. Berechnen Sie die Schnittmenge von s1 und s2 erneut.

s1_s2_int = s1.intersection(s2)
print(f"Schnittmenge von {s1} und {s2} ist: {s1_s2_int}")


# 6. Prüfen Sie mit disjoint() erneut, ob beide Mengen disjunkt sind.

if s1.isdisjoint(s2):
    print(f"Sets {s1} und {s2} haben keine gemeinsame Werte")
else:
    print(f"Sets {s1} und {s2} haben gemeinsame Werte")


# 7. Vereinigen Sie beide Mengen mit union(). Speichern Sie das Ergebnis dabei
# in der Variablen s1_s2_union ab. Was enthält die eben erstellte Variable?

s1_s2_union = s1.union(s2)
print(f"Vereinigung von {s1} und {s2} ist: {s1_s2_union}")
