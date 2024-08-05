# Schreibe eine Funktion permutate_string(), die eine
# zufällige Permutation eines Namens zurückgibt.
# Nutze dazu die Shuffle Methode des random Moduls.

# Parameter: name
# Rückgabewert: String
# stefan = fetsan

# Hinweis: ein String ist KEINE mutable Sequence!

from random import shuffle


def permutate_string(s):
    seq = list(s)
    shuffle(seq)
    return "".join(seq)


print(permutate_string("stefan"))
