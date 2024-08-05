"""
Implementiere ein Python-Skript, das eine neue Bestellung in der Webshop-Datenbank anlegt.

Den SQL-Code zum Anlegen dieser Webshop-Datenbank findest du in:
`aufgabe_webshop_datenbank_anlegen.sql`.

=> Führe diesen Code EINMALIG aus!!!
--------------------------------------------------------------------------

Die Bestellung soll aus mehreren Artikeln bestehen. Für jede Bestellung
wird eine order in der Tabelle orders angelegt.
Die einzelnen Artikel für diese Bestellung finden sich in Orderpositionen.
Dafür ist die orders.id notwendig.

Die orderid einer neu eingetragenen Order erhalten:
D.h. wenn eine Order eingetragen wird, erhält man NACH dem execute die orderid.
order_id = cursor.lastrowid
------------------------------------------------------------

Wenn eine ungültige Produkt-ID in den Bestellpositionen enthalten ist,
soll die gesamte Transaktion fehlschlagen und ein Rollback durchgeführt
werden, um alle Änderungen rückgängig zu machen. Das betrifft vor allem die schon eingetragene Order.


Beispiel für eine valide Aktion:
--------------------------------
order_details = [
                {"product_id": 1, "quantity_ordered": 1},  # Harley Davidson
                {"product_id": 4, "quantity_ordered": 2},  # Ferrari
            ]
customer_id = 1  # John Doe
todays_date = date.today()

orderid = create_order(cursor, order_details, customer_id, todays_date)
Order with ID 15 placed successful

Beispiel für eine ungültige Aktion
--------------------------------
die product_id 999 existiert nicht
(order UND orderpostions dürfen nicht in der DB eingetragen sein)

order_details = [
                {"product_id": 1, "quantity_ordered": 1},  # Harley Davidson
                {"product_id": 999, "quantity_ordered": 2},  # Ferrari
            ]
customer_id = 1  # John Doe
todays_date = date.today()

Failed to create order: 1452 (23000): Cannot add or update a child row: a foreign key constraint failed.
"""
import mysql.connector
from mysql.connector import Error
from datetime import date

ORDER_DETAILS = list[dict[str, int]]

def create_order(cursor,
                order_details: ORDER_DETAILS,
                customer_id: int,
                order_date: date) -> None:
    """Create an order in the webshop.

    Does Rollback if order fails.

    Args:
        cursor: current database cursor
        order_details: list of order positions
        customer_id: int
        order_date: datetime object

    Hints:
        orderposition format:
        {"product_id": 1, "quantity_ordered": 1},

    Return:
        True if order placed successfully

    Raises:
        Exception if order could not be placed successfully.
    """

def main():
    # create connection, place order. Rollback order if error occurs.
    order_details: ORDER_DETAILS = [
        {"product_id": 1, "quantity_ordered": 1},  # Harley Davidson
        {"product_id": 2, "quantity_ordered": 42},  # Ferrari
    ]
    customer_id = 1
    todays_date = date.today()

    # place order
    create_order(cursor, order_details, customer_id, todays_date)

if __name__ == "__main__":
    main()
