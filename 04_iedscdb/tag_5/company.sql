-- Erstelle eine Datenbank lege die Tabellen an.
-- Aufgaben ab Zeile 50. Happy Coding!

CREATE DATABASE if not exists companydb;
use companydb;

CREATE TABLE Employee (
Employee_id int AUTO_INCREMENT PRIMARY KEY,
First_name VARCHAR(50),
Last_name VARCHAR(50),
Salary int,
Joining_date Date,
Departement VARCHAR(50)
);

CREATE TABLE reward (
Employee_ref_id int,
date_reward Date,
amount int,
FOREIGN KEY (Employee_ref_id) REFERENCES Employee(Employee_id)
);

-- Füge Testdaten ein

INSERT INTO Employee (Employee_id, First_name, Last_name, Salary, Joining_date, Departement)
VALUES (1, 'Bob', 'Kinto', 1000000, "2019-01-20", "Finance");
INSERT INTO Employee (Employee_id, First_name, Last_name, Salary, Joining_date, Departement)
VALUES (2, 'Jerry', 'Kansxo', 6000000, "2019-01-15", "IT");
INSERT INTO Employee (Employee_id, First_name, Last_name, Salary, Joining_date, Departement)
VALUES (3, 'Philip', 'Jose', 8900000, "2019-02-05", "Banking");
INSERT INTO Employee (Employee_id, First_name, Last_name, Salary, Joining_date, Departement)
VALUES (4, 'John', 'Abraham', 2000000, "2019-02-25", "Insurance");
INSERT INTO Employee (Employee_id, First_name, Last_name, Salary, Joining_date, Departement)
VALUES (5, 'Michael', 'Mathew', 2200000, "2019-02-28", "Finance");
INSERT INTO Employee (Employee_id, First_name, Last_name, Salary, Joining_date, Departement)
VALUES (6, 'Alex', 'chreketo', 4000000, "2019-05-10", "IT");
INSERT INTO Employee (Employee_id, First_name, Last_name, Salary, Joining_date, Departement)
VALUES (7, 'Yohan', 'Soso', 1230000, "2019-06-20", "Banking");

-- rewards
INSERT INTO reward (Employee_ref_id, date_reward, amount) VALUES (1, '2019-05-11', '1000');
INSERT INTO reward (Employee_ref_id, date_reward, amount) VALUES (2, '2019-02-15', '5000');
INSERT INTO reward (Employee_ref_id, date_reward, amount) VALUES (3, '2019-04-22', '2000');
INSERT INTO reward (Employee_ref_id, date_reward, amount) VALUES (1, '2019-06-20', '8000');


-- AUFGABEN
-- 1. Get all employees
SELECT
    *
FROM
    employee;

-- 2. Display the first name and last name of all employees
SELECT
    First_name, Last_name
FROM
    employee;

-- 3. Display all the values of the “First_Name” column using the alias “Employee Name”
SELECT
    First_name AS "Employee Name"
FROM
    employee;

-- 4. Get all “Last_Name”s in lowercase
SELECT
    LOWER(Last_name)
FROM
    employee;

-- 5. Get all “Last_Name”s in uppercase
SELECT
    UPPER(Last_name)
FROM
    employee;

-- 6. Get unique “DEPARTMENT”s
SELECT DISTINCT
    Departement
FROM
    employee;

-- 7. Get the first 4 characters of the “FIRST_NAME” column

SELECT
    SUBSTRING(First_name, 1, 4)
FROM
    employee;

-- 12. Get the employee’s first name after replacing ‘o’ with ‘#’

SELECT
    REPLACE(First_name, "o", "#")
FROM
    employee;

-- 13. Get the employee’s last name and first name in a single column separated by a ‘_’

SELECT
   CONCAT(Last_name, "_", First_name)
FROM
    employee;

-- 14. Get the year, month, and day from the “Joining_date” column

SELECT
    YEAR(Joining_date),
    MONTH(Joining_date),
    DAY(Joining_date)
FROM
    employee;

-- 15. Get all employees in ascending order by first name

SELECT
    *
FROM
    employee
ORDER BY
    First_name;

-- 16. Get all employees in descending order by first name

SELECT
    *
FROM
    employee
ORDER BY
    First_name DESC;

-- 17. Get all employees in ascending order by first name and descending order by salary

SELECT
    *
FROM
    employee
ORDER BY
    First_name, Salary DESC;

-- 18. Get employees whose first name is “Bob”

SELECT
    *
FROM
    employee
WHERE
    First_name = "Bob";

-- 19. Get employees whose first name is “Bob” or “Alex”

SELECT
    *
FROM
    employee
WHERE
    First_name IN ("Bob", "Alex");

-- 21. Get all the details about employees whose first name begins with ‘B’

SELECT
    *
FROM
    employee
WHERE
    First_name LIKE "B%";

-- 22. Get all the details about employees whose first name contains ‘o’

SELECT
    *
FROM
    employee
WHERE
    First_name LIKE "%o%";

-- 23. Get all the details of the employees whose first name ends with ‘n’

SELECT
    *
FROM
    employee
WHERE
    First_name LIKE "%n";

-- 26. Get all the details of employees whose salary is over 3,000,000

SELECT
    *
FROM
    employee
WHERE
    Salary > 3000000;

-- 28. Get all the details about employees with a salary between 2,000,000 and 5,000,000

SELECT
    *
FROM
    employee
WHERE
    Salary BETWEEN 2000000 AND 5000000;

-- 30. Get all the details about employees whose joining year is “2019”

SELECT
    *
FROM
    employee
WHERE
    YEAR(Joining_date) = 2019;

-- 31. Get all the details on employees whose participation month (Joining_date) is “January”

SELECT
    *
FROM
    employee
WHERE
    MONTH(Joining_date) = 1;


SELECT
    *
FROM
    employee
WHERE
    MONTHNAME(Joining_date) = "January";

-- 32. Get all the details of the employees who joined before March 1, 2019

SELECT
    *
FROM
    employee
WHERE
    Joining_date < "2019-03-01";

-- 33. Get all the details on employees who joined after March 31, 2019

SELECT
    *
FROM
    employee
WHERE
    Joining_date > "2019-03-31";

-- 38. Get the employee’s department and total salary, grouped by department

SELECT
    *
FROM
    employee
WHERE
    Joining_date < "2019-03-01";

-- 39. Get the department and total salary, grouped by department,
-- and sorted by total salary in descending order

SELECT
    Departement,
    SUM(Salary) AS Total_salary
FROM
    employee
GROUP BY
    Departement
ORDER BY
    Total_salary DESC;


-- 40. Get the department, the number of employees in that department,
-- and the total salary grouped by department,
-- and sorted by total salary in descending order

SELECT
    Departement,
    COUNT(*) AS Employees_number,
    SUM(Salary) AS Total_salary
FROM
    employee
GROUP BY
    Departement
ORDER BY
    Total_salary DESC;

-- 41. Get the average salary by department in ascending order of salary

SELECT
    Departement,
    AVG(Salary) AS Average_salary
FROM
    employee
GROUP BY
    Departement
ORDER BY
    Average_salary;

-- 42. Get the maximum salary by department in ascending order of salary

SELECT
    Departement,
    MAX(Salary) AS Max_salary
FROM
    employee
GROUP BY
    Departement
ORDER BY
    Max_salary;

-- 43. Get the number of employees grouped by year and month of membership

SELECT
    COUNT(*) AS Employees_number,
    CONCAT(YEAR(Joining_date), "-", MONTH(Joining_date)) AS Join_year_month
FROM
    employee
GROUP BY
    YEAR(Joining_date), MONTH(Joining_date);
