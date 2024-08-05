"""
1. Aufgabe (Ohne Python, auf CommandLine oder Workbench)
-------------
a. ) Erstelle eine neue Datebank hospital_management
b. ) Erstelle zwei Tabellen: Doctor und Hospital

Diese Testdaten sollen eingefügt werden, setze den entsprechenden
Foreign Key in der Tabelle.


INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) 
VALUES 
(1, 'Mayo Clinic', 200), 
(2, 'Cleveland Clinic', 400), 
(3, 'Johns Hopkins', 1000), 
(4, 'UCLA Medical Center', 1500);

INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
VALUES 
(101, 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
(102, 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
(103, 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
(104, 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
(105, 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
(106, 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
(107, 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
(108, 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);

Finde für die Tabellen die entsprechenden Datentypen und lege die Tabellen an.
Zeichne für die beiden Tabellen ein ER-Diagramm (Papier oder Software)

2. Aufgabe (mit Python)
-------------
Schreibe ein Python-Programm und verbinde dich mit der Mysql-Datenbank.
Implementiere die Funktionalität, um die Details eines gegebenen Arztes aus der
Arzttabelle und des Krankenhauses aus der Krankenhaustabelle zu lesen, d.h.
lese Datensätze aus der Krankenhaus- und Arzttabelle gemäß der gegebenen
Krankenhaus- und Arzt-ID.

get_hospital_details(2)
get_doctor_details(105)

b.) Erweiterung (optional): es können auch jeweils mehrere Ids übergeben werden.
get_hospital_details(2, 4, 3)
get_doctor_details(105, 106)

OUTPUT Beispiel:
Printing Hospital record
Hospital Id: 2
Hospital Name: Cleveland Clinic
Bed Count: 400

Printing Doctor record
Doctor Id: 105
Doctor Name: Linda
Hospital Id: 3
Joining Date: 2004-06-04
Specialty: Garnacologist
Salary: 42000
Experience: None

3. Aufgabe (Mit Python)
---------------
Suche nach allen Ärzten, deren Gehalt höher ist als der eingegebene Betrag und deren Fachgebiet mit dem eingegebenen Fachgebiet übereinstimmt.

get_specialist_doctors_list("Garnacologist", 30000)

Printing doctors whose specialty is Garnacologist and salary greater than 30000 
Doctor Id:  105
Doctor Name: Linda
Hospital Id: 3
Joining Date: 2004-06-04
Specialty: Garnacologist
Salary: 42000
Experience: None 
 
Doctor Id:  107
Doctor Name: Richard
Hospital Id: 4
Joining Date: 2014-08-21
Specialty: Garnacologist
Salary: 32000
Experience: None 

4. Aufgabe (Mit Python)
------------
Implementiere die Funktion zum Abrufen aller Ärzte gemäß der angegebenen
Krankenhausnummer. Sie müssen den Namen des Krankenhauses eines Arztes
anzeigen.

get_doctors(2)

Hospitals of Id 2:
Doctor_Id: 103
Doctor_Name: Susan
Hospital_Id: 2
Joining_Date: 2016-05-19
Speciality: Garnacologist
Salary: 25000
Experience: None
Hospital_Name: Cleveland Clinic
Bed_Count: 400
"""
