from __future__ import annotations


class Kunde:
    def __init__(self, name: str, kunde_id: int) -> None:
        self.name = name
        self.kunde_id = kunde_id
        self.kontos = []


class Konto:
    def __init__(self,
                nummer: int,
                inhaber: Kunde,
                anfangsguthaben: float,
                bank: Bank) -> None:

        self.nummer = self.nummer
        self.inhaber = inhaber
        self.guthaben = anfangsguthaben
        self.bank = bank


    def einzahlung(self, betrag: float) -> None:
        self.guthaben += betrag
        print(f"Betrag von {} Euro wurde erfolgreich eingezahlt.")


    def kontostandabfragen(self):
        pass


class Bank:
    def __init__(self, name: str) -> None:
        self.name = name
        self.kunden = []
        self.kontos = []

    
    def kunde_hinzufuegen(self, kundenname: str, kunde_id: int) -> bool:

        if kunde_id in [kunde.kunde_id for kunde in self.kunden]:
            return False
        
        kunde = Kunde(kundenname, kunde_id)
        self.kunden.append(kunde)

        #  konto_oeffnen()

        return True


    def kunde_entfernen(self, kunde: Kunde) -> bool:
        if kunde not in self.kunden:
            return False
        self.kunden.remove(kunde)
        return True

    
    def konto_oeffnen(self, kontonummer, ) -> Konto:
        if kontonummer in [konto.nummer for konto in self.kontos]:
            return False


    def konto_schliessen(self):
        pass


class Sparkonto(Konto):
    def __init__(self,
                inhaber: Kunde,
                anfangsguthaben: float,
                zinssatz: float) -> None:

        super().__init__(inhaber, anfangsguthaben)
        self.zinssatz = zinssatz


    def abhebung(self, betrag: float) -> bool:
        if self.guthaben < betrag:
            return False

        self.guthaben -= betrag
        return True


    def zinsberechnung(self) -> None:
        pass


class Girokonto(Konto):
    def __init__(self,
                inhaber: Kunde,
                anfangsguthaben: float,
                überziehungslimit: float) -> None:

        super().__init__(inhaber, anfangsguthaben)
        self.überziehungslimit = überziehungslimit


    def abhebung(self, betrag: float) -> None:
        if (self.guthaben + self.überziehungslimit) < betrag:
            return False

        self.guthaben -= betrag
        return True