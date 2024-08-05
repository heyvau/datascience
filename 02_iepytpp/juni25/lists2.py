# Aufgaben:

# Gegeben sei die folgende Liste:

l = [42, 109, -30]
l_copy = l.copy()
print(l)
print(l_copy)


# 1. Recherchieren Sie die Arbeitsweise der Methoden insert() und append() und zeigen Sie, an einem
# selbst gewählten Beispiel, wie die Methode insert() in die Methode append() überführt werden kann.

s = "hi"

l.append(s)
print(f"Methode append: {l}")

l_copy.insert(len(l_copy), s)
print(f"Methode append: {l_copy}")


# 2. Die Methode pop() löscht das letzte Element einer Liste. Entwickeln Sie eine Idee, wie dies alternativ
# mit dem Schlüsselwort del umgesetzt werden kann.

l.pop()
print(f"Methode pop: {l}")

last_item_index = len(l_copy) - 1
del l_copy[last_item_index]
print(f"Schlüsselwort del: {l_copy}")
