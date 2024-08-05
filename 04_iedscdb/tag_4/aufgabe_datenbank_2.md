# Aufgabe Datenbank (SCHWER)

**Aufgabe: Online-Shop Datenbankdesign**

Sie sind beauftragt worden, eine Datenbank für einen Online-Shop zu entwerfen. Der Shop verkauft Produkte und verwaltet Bestellungen von Kunden. Das Datenbankdesign sollte die folgenden Anforderungen erfüllen:

1. Erstellen Sie vier Tabellen: `Produkte`, `Kunden`, `Bestellungen` und `Bestellpositionen`.

2. Die Tabelle `Produkte` sollte Informationen zu den im Shop erhältlichen Produkten speichern. Jedes Produkt hat eine eindeutige Produkt-ID, Name, Beschreibung und Preis.

3. In der Tabelle `Kunden` sollten Informationen über die Shop-Kunden festgehalten werden. Jeder Kunde hat eine eindeutige Kunden-ID, Vorname, Nachname, E-Mail und Adresse.

4. Die Tabelle `Bestellungen` sollte die Bestellungen der Kunden verfolgen. Jede Bestellung erhält eine eindeutige Bestell-ID, die einem Kunden zugeordnet ist. Die Tabelle sollte auch das Bestelldatum und den Bestellstatus speichern.

5. Die Tabelle `Bestellpositionen` sollte die bestellten Produkte für jede Bestellung verfolgen. Jede Bestellposition hat eine eindeutige Position-ID und ist einer Bestellung sowie einem Produkt zugeordnet. Sie sollte auch die Menge und den Gesamtpreis der Position speichern.

6. Erstelle Beziehungen zwischen den Tabellen. Ein Produkt sollte einer
   Bestellposition und somit einer Bestellung zugeordnet sein. Eine Bestellung
sollte einem Kunden zugeordnet sein.

7. Verwende geeignete Datentypen, Primärschlüssel und Fremdschlüssel für jede Tabelle.

Die Aufgabe besteht darin, SQL-Code zu entwerfen, um das Datenbankdesign für den Online-Shop umzusetzen. 
Es sollten CREATE TABLE-Anweisungen verwenden werden, um die Tabellen zu erstellen, um die Beziehungen zwischen den Tabellen festzulegen.

Zeichne einfache UML-Diagramme, um die Tabellen zu visualisieren.
Lege die Tabellen in MySQL an. Erstelle dazu eine neue Datenbank.
