# Aufgabe Tuple Liste

# Erstelle eine Funktion range_list, die eine Liste aus Tuples
# in folgender Form zurückgibt

# x = [(15, 19), (20, 24), (25, 29), ... (65, 69), (70, 74), (75, 79), (80, 84)]

RANGE = 5
START_VALUE = 15
END_VALUE = 85


def range_list():
    r = range(START_VALUE, END_VALUE, RANGE)
    return tuple(
        [(x, x + (RANGE - 1)) for x in r]
    )


print(range_list())
