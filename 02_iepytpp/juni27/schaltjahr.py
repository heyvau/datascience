jahr = int(input("Jahr: "))

if (not jahr % 4) and (jahr % 100) or (not jahr % 400):
    print(f"Ja, das Jahr {jahr} ist ein Schaltjahr")
else:
    print(f"Nein, das Jahr {jahr} ist kein Schaltjahr")

