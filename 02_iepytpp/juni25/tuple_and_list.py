# Gegeben sei das folgende tuple t:

t = (1, 20, 30)

# Aufgaben:

# 1. Lesen Sie den ersten, zur Verfügung stehenden, Index von t aus.

print(f"Der erste Index von {t}: {t[0]}")


# 2. Versuchen Sie diesen Wert auf 10 zu ändern.

# t[0] = 10 - funktioniert nicht, weil Tupel unveränderbar ist


# 3. Konvertieren Sie das Tuple nun in eine Liste mit der Funktion list().

l = list(t)


# 4. Lesen Sie die in 3. erstellte Liste nun aus und ändern Sie daraufhin den ersten Index auf 10.

print(f"Die Liste {l} ist veränderbar")
l[0] = 10
print(f"Stimmt: {l}")


# 5. Konvertieren Sie die Liste nun zurück in das Tuple mit dem Namen t unter verwendung der Funktion tuple().

t = tuple(l)
print(f"Und jetzt bin ich, {t}, wieder ein Tupel und kann nicht geändert werden")
