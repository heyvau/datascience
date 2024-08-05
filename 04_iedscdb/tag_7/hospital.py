import mysql.connector


account = {
    "host": "localhost",
    "user": "root",
    "password": "12345",
    "port": 3306,
    "database": "hospital_management"
}


def connect_db(account):
    def inner(func):
        def wrapper(*args, **kwargs):
            with mysql.connector.connect(**account) as conn:
                try:
                    return func(*args, conn=conn, **kwargs)

                except mysql.connector.Error as e:
                    conn.rollback()
                    print(f"Es ist ein DB-Fehler aufgetreten: {e}")

                except Exception as e:
                    conn.rollback()
                    print(f"Es ist ein unbekannter Fehler aufgetreten: {e}")
        return wrapper
    return inner


@connect_db(account)
def get_hospital_details(*args, **kwargs):
    """
    Get hospital details by id.
    """
    ids = ", ".join(["%s"] * len(args))

    sql_statement = f"""
        SELECT
            *
        FROM
            Hospital
        WHERE
            Hospital_Id IN ({ids})
    """
    conn = kwargs.get("conn")
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(sql_statement, args)
        res = cursor.fetchall()
        return res


@connect_db(account)
def get_doctor_details(*args, **kwargs):
    """
    Get doctor details by id.
    """
    ids = ", ".join(["%s"] * len(args))

    sql_statement = f"""
        SELECT
            *
        FROM
            Doctor
        WHERE
            Doctor_Id IN ({ids})
    """
    conn = kwargs.get("conn")
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(sql_statement, args)
        res = cursor.fetchall()
        return res


@connect_db(account)
def get_specialist_doctors_list(speciality, salary, **kwargs):
    print(
        f"\n*** Printing doctors whose specialty is {speciality} and salary greater than {salary} ***\n"
    )
    sql_statement = f"""
        SELECT
            *
        FROM
            Doctor
        WHERE
            Speciality = %s AND Salary > %s
    """
    values = (speciality, salary)
    conn = kwargs.get("conn")
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(sql_statement, values)
        res = cursor.fetchall()
        return res


@connect_db(account)
def get_doctors_by_hospital(hospital_id, **kwargs):
    print(
        f"\n*** Printing doctors whose Hospital Id is {hospital_id} ***\n"
    )
    sql_statement = f"""
        SELECT
            *
        FROM
            Doctor AS d
        INNER JOIN
            Hospital AS h
        ON
            d.Hospital_Id = h.Hospital_Id
        WHERE
            d.Hospital_Id = %s
    """
    values = (hospital_id, )
    conn = kwargs.get("conn")
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(sql_statement, values)
        res = cursor.fetchall()
        return res


def print_details(record):
    print(f"Printing {list(record.keys())[0].split('_')[0]} record\n")
    for k, v in record.items():
        print(f"{k.replace('_', ' ')}: {str(v)}")
    print("-------------------\n")


def main():
    
    [print_details(_) for _ in get_hospital_details(3)]
    [print_details(_) for _ in get_doctor_details(105, 108)]
    [print_details(_) for _ in get_specialist_doctors_list("Garnacologist", 30000)]
    [print_details(_) for _ in get_doctors_by_hospital(2)]

if __name__ == "__main__":
    main()