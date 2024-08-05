import mysql.connector
from mysql.connector import Error
from datetime import date


account = {
    "host": "localhost",
    "user": "root",
    "password": "12345",
    "port": 3306,
    "database": "Webshop"
}


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
    try:
        sql_statement = """
            INSERT INTO
                orders (customer_id, order_date)
            VALUES
                (%s, %s)
        """
        values = (customer_id, order_date)
        cursor.execute(sql_statement, values)
        order_id = cursor.lastrowid

        order_details = [
            (order_id, product["product_id"], product["quantity_ordered"])
            for product
            in order_details]

        sql_statement = """
            INSERT INTO
                order_positions (order_id, product_id, anzahl)
            VALUES
                (%s, %s, %s)
        """
        cursor.executemany(sql_statement, order_details)

    except Error as e:
        print(f"Es ist ein DB-Fehler aufgetreten: {e}")

    except Exception as e:
        print(f"Es ist ein unbekannter Fehler aufgetreten: {e}")
    else:
        return True


def main(account):
    
    order_details: ORDER_DETAILS = [
        {"product_id": 1, "quantity_ordered": 1},  # Harley Davidson
        {"product_id": 2, "quantity_ordered": 42},  # Ferrari
    ]
    customer_id = 1
    todays_date = date.today()

    with mysql.connector.connect(**account) as conn:
        with conn.cursor() as cursor:
            result = create_order(cursor, order_details, customer_id, todays_date)
            if result:
                conn.commit()
            else:
                conn.rollback()


if __name__ == "__main__":
    main(account)