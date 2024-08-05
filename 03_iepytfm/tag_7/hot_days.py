"""
HOT DAYS

Schreibe eine Funktion get_hot_work_days(), die aus der Input-Liste weekday_temperatures  eine neue Liste erstellt und diese zurückgibt.
Diese neue Liste soll nur Tage enthalten, die nicht am Wochenende sind und Temperaturen größer gleich 30 Grad Celcius hatten.
Die Einträge in der neuen Liste sollen als Tupel dargestellt werden (Datum, Temperatur)

Ergebnis:
[('2019-07-15', 31), ('2019-07-16', 33), ('2019-07-19', 30), ('2019-07-23', 31)]

Hinweise: diese Aufgabe optional mit list comprehension oder funktional (map,
filter) lösen.
Nutze Typehints!
"""

THRESHOLD = 30
WEEKENDS_DAYS = ["Saturday", "Sunday"]

weekday_temperatures = [
    {"day": "Monday", "date": "2019-07-15", "temperature": 31},
    {"day": "Tuesday", "date": "2019-07-16", "temperature": 33},
    {"day": "Wednesday", "date": "2019-07-17", "temperature": 27},
    {"day": "Thursday", "date": "2019-07-18", "temperature": 25},
    {"day": "Friday", "date": "2019-07-19", "temperature": 30},
    {"day": "Saturday", "date": "2019-07-20", "temperature": 31},
    {"day": "Sunday", "date": "2019-07-21", "temperature": 29},
    {"day": "Monday", "date": "2019-07-22", "temperature": 25},
    {"day": "Tuesday", "date": "2019-07-23", "temperature": 31},
    {"day": "Wednesday", "date": "2019-07-24", "temperature": 26},
    {"day": "Thursday", "date": "2019-07-25", "temperature": 23},
    {"day": "Friday", "date": "2019-07-26", "temperature": 22},
    {"day": "Saturday", "date": "2019-07-27", "temperature": 23},
    {"day": "Sunday", "date": "2019-07-28", "temperature": 32},
    {"day": "Sunday", "date": "2019-07-28", "temperature": 32},
]


# def get_hot_work_days(temeratures_list: list) -> list[tuple]:
#     """
#     Die Funktion nimmt eine Temperaturliste ein und gibt eine neue Liste zurück,
#     die nur Tage enthaltet, die nicht am Wochenende sind und Temperaturen größer
#     gleich 30 Grad Celcius haben.
#     """

#     return [
#         (w_day["date"], w_day["temperature"])
#         for w_day in temeratures_list
#         if w_day["day"] not in WEEKENDS_DAYS and
#         w_day["temperature"] >= THRESHOLD
#     ]


# ---------------------------------- Version 2 ----------------------------------


def is_hot_work_day(day: dict) -> bool:
    """
    Die Funktion gibt True zurück, wenn der angegebene Tag nicht am Wochenende ist
    und Temperatur größer gleich 30 Grad Celcius hat. Ansonsten - False.
    """

    return day["day"] not in WEEKENDS_DAYS and day["temperature"] >= THRESHOLD


def get_hot_work_days(temeratures_list: list) -> list[tuple]:
    """
    Die Funktion nimmt eine Temperaturliste ein und gibt eine neue Liste zurück,
    die nur Tage enthaltet, die nicht am Wochenende sind und Temperaturen größer
    gleich 30 Grad Celcius haben.
    """
    filtered_days = filter(is_hot_work_day, temeratures_list)
    return list(map(lambda day: (day["date"], day["temperature"]), filtered_days))


def main():
    """
    Hauptfunktion
    """

    print(get_hot_work_days(weekday_temperatures))


if __name__ == "__main__":
    main()