CREATE DATABASE animal_park;

USE animal_park;

CREATE TABLE IF NOT EXISTS species(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    description TEXT
);

CREATE TABLE IF NOT EXISTS animal(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    description TEXT,
    species_id INT,
    birthdate DATE,
    FOREIGN KEY (species_id) REFERENCES species(id)
);

INSERT INTO species(name, description)
VALUES 
    ("Lion", "The lion (Panthera leo)
    is a large cat of the genus Panthera,
    native to Africa and India."),
    ("Penguin", "Penguins are a group
    of aquatic flightless birds
    from the family Spheniscidae
    of the order Sphenisciformes.");

INSERT INTO animal(name, description, species_id, birthdate)
VALUES
    ("Charlie", "male", 3, "2015-04-17"),
    ("Martin", "male", 4, "2020-08-23"),
    ("Lucy", "female", 4, "2017-10-11"),
    ("George", "male", 4, "2019-03-10"),
    ("Freya", "female", 3, "2010-07-27");

SELECT animal.name, animal.birthdate, species.name
FROM animal, species
WHERE animal.species_id = species.id
AND animal.description = "female";