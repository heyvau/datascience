"""
(MITTEL)
Gegeben ist eine Variable x im globalen Scope.
Schreibe eine Funktion increment, die x im globalen Scope um eins erhöht.
"""


x = 4

def increment():
    global x 
    x += 1

increment()
print(x)

