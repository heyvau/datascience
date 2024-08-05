"""
1.  (MITTEL)
Erstelle eine Funktion filter_integer_data, die eine Liste
als Parameter entgegennimmt und jedes Element prüft, ob es vom
Typ integer ist. Der Rückgabewert der Liste ist eine Liste mit)
Integerwerten. Nutze zum Prüfen des Typs die Funktion type() oder isinstance()

result = filter_integer_data(["a", 3, 1, 3.3])
Result: [3, 1]
"""

# Version 1

# def filter_integer_data(liste):
#     return list(filter(lambda x: isinstance(x, int), liste))

# Version 2

# def filter_integer_data(liste):
#     res = []
#     for i in liste:
#         if isinstance(i, int):
#             res.append(i)
#     return res

# Version 3

def filter_integer_data(liste):
    return [i for i in liste if isinstance(i, int)]

print(filter_integer_data(["a", 3, 1, 3.3]))


"""
2. (MITTEL)
Erstelle eine Funktion check_values, die eine Liste mit float-Werten und einen
tupel übergeben bekommt. Die Funktion prüft, ob alle Elemente
im geschlossenen Interval [a, b] liegen. Der Rückgabewert ist ein boolean.
Erinnerung: geschlossenes Interval bedeutet, das das Intervall alle Werte inklusive der
Grenzwerte zwischen zwei bestimmten Zahlen einschließt
"""


def check_values(values, interval):
    for i in values:
        if i < interval[0] or i > interval[1]:
            return False
    return True

values = [2, 2.2, 4, 2.3, 1.0]
interval = (1, 5.3)
result = check_values(values, interval)
print(result)

