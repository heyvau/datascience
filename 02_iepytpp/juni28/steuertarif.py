# Die deutsche Einkommensteuer wird nach § 32a
# aus dem Einkommensteuergesetz (EStG) berechnet:

# § 32a Einkommensteuertarif

# (1) 1 Die tarifliche Einkommensteuer bemisst sich 
# nach dem auf volle Euro abgerundeten zu versteuernden Einkommen. 

# 2 Sie beträgt im Veranlagungszeitraum 2023 vorbehaltlich 
# der §§ 32b, 32d, 34, 34a, 34b und 34c jeweils in Euro für zu versteuernde Einkommen

# 1.
#     bis 10 908 Euro (Grundfreibetrag):
#     0;
# 2.
#     von 10 909 Euro bis 15 999 Euro:
#     (979,18 · y + 1 400) · y;
# 3.
#     von 16 000 Euro bis 62 809 Euro:
#     (192,59 · z + 2 397) · z + 966,53;
# 4.
#     von 62 810 Euro bis 277 825 Euro:
#     0,42 · x – 9 972,98;
# 5.
#     von 277 826 Euro an:
#     0,45 · x – 18 307,73.

# 3 Die Größe „y“ ist ein Zehntausendstel
# des den Grundfreibetrag übersteigenden Teils
# des auf einen vollen Euro-Betrag abgerundeten zu versteuernden Einkommens.

# 4 Die Größe „z“ ist ein Zehntausendstel des 15 999 Euro übersteigenden Teils
# des auf einen vollen Euro-Betrag abgerundeten zu versteuernden Einkommens.

# 5 Die Größe „x“ ist
# das auf einen vollen Euro-Betrag abgerundete zu versteuernde Einkommen.

# 6 Der sich ergebende Steuerbetrag ist
#  auf den nächsten vollen Euro-Betrag abzurunden.




# Aufgabe:

# Erstellen Sie ein Python-Skript,
# dass den die oben beschriebene Berechnung der Einkommensteuer implementiert.
# Testen Sie Ihren Code daraufhin mit einigen, selbst gewählten, Werten.

max_grundfreibetrag = 10908

def erhalten_einkommensbetrag():

    while True:
        einkommen_str = input("Mein Einkommen beträgt: ")

        try:
            einkommensbetrag = float(einkommen_str)
            break

        except ValueError:
            print("Angabe ist nicht korrekt. Probiere noch einmal.")

    return einkommensbetrag
    

def xyz_berechnung(betrag, subtr=0, koef=1):
    return koef * (betrag - subtr)


def einkommensteuer_berechnung(einkommen):

    einkommensteuer = 0

    abgerund_einkommen = int(einkommen)

    x = xyz_berechnung(abgerund_einkommen)

    if abgerund_einkommen in range(10909, 16000):

        y = xyz_berechnung(abgerund_einkommen, max_grundfreibetrag, 0.0001)
        einkommensteuer = (979.18 * y + 1400) * y

    elif abgerund_einkommen in range(16000, 62810):

        z = xyz_berechnung(abgerund_einkommen, 15999, 0.0001)
        einkommensteuer = (192.59 * z + 2397) * z + 966.53

    elif abgerund_einkommen in range(62810, 277826):

        einkommensteuer = 0.42 * x - 9972.98

    elif (abgerund_einkommen >= 277826):

        einkommensteuer = 0.45 * x - 18307.73
    
    else:

        einkommensteuer = 0 

    return int(einkommensteuer)


if __name__ == "__main__":

    mein_einkommen = erhalten_einkommensbetrag()

    einkommensteuer = einkommensteuer_berechnung(mein_einkommen)

    print(f"Deine Einkommensteuer beträgt {einkommensteuer} Euro")
