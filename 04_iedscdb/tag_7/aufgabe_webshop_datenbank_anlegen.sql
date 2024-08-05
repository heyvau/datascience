-- Datenbank anlegen
CREATE DATABASE IF NOT EXISTS Webshop;
USE Webshop;

-- Kategorie-Tabelle anlegen
CREATE TABLE categories(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL
);

INSERT INTO categories (name) VALUES ('Classic Cars');
INSERT INTO categories (name) VALUES ('Motorcycles');
INSERT INTO categories (name) VALUES ('Planes');
INSERT INTO categories (name) VALUES ('Ships');

-- Produkttabelle anlegen (1-N zu Kategorie)
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

INSERT INTO products (name, category_id) VALUES ('Harley Davidson', 2);
INSERT INTO products (name, category_id) VALUES ('Boeing 747', 3);
INSERT INTO products (name, category_id) VALUES ('Titanic', 4);
INSERT INTO products (name, category_id) VALUES ('Ferrari', 1);

-- Tags (Schlagwort-Tabelle anlegen)
CREATE TABLE tags (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL
);

INSERT INTO tags (name) VALUES ('Luxury');
INSERT INTO tags (name) VALUES ('Vintage');
INSERT INTO tags (name) VALUES ('Sport');
INSERT INTO tags (name) VALUES ('Modern');

-- Tabelle mit Tags für Produkte anlegen (N:M)
CREATE TABLE products_tags (
    product_id INT,
    tag_id INT,
    PRIMARY KEY (product_id, tag_id),
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

INSERT INTO products_tags (product_id, tag_id) VALUES (1, 2); -- Harley Davidson - Vintage
INSERT INTO products_tags (product_id, tag_id) VALUES (2, 4); -- Boeing 747 - Modern
INSERT INTO products_tags (product_id, tag_id) VALUES (3, 2); -- Titanic - Vintage
INSERT INTO products_tags (product_id, tag_id) VALUES (4, 3); -- Ferrari - Sport
INSERT INTO products_tags (product_id, tag_id) VALUES (4, 1); -- Ferrari - Luxury

-- Kunden-Tabelle anlegen
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(120) NOT NULL,
    last_name VARCHAR(120) NOT NULL
);

INSERT INTO customers (first_name, last_name) VALUES ('John', 'Doe');
INSERT INTO customers (first_name, last_name) VALUES ('Jane', 'Smith');
INSERT INTO customers (first_name, last_name) VALUES ('Emily', 'Jones');
INSERT INTO customers (first_name, last_name) VALUES ('Michael', 'Brown');

-- Profil-Tabelle anlegen
CREATE TABLE profile (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT UNIQUE,
    image VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

INSERT INTO profile (customer_id, image) VALUES (1, 'john_doe.jpg');
INSERT INTO profile (customer_id, image) VALUES (2, 'jane_smith.jpg');
INSERT INTO profile (customer_id, image) VALUES (3, 'emily_jones.jpg');
INSERT INTO profile (customer_id, image) VALUES (4, 'michael_brown.jpg');

-- Bestellungs-Tabelle anlegen
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

INSERT INTO orders (customer_id, order_date) VALUES (1, '2024-07-01');
INSERT INTO orders (customer_id, order_date) VALUES (2, '2024-07-02');
INSERT INTO orders (customer_id, order_date) VALUES (3, '2024-07-03');
INSERT INTO orders (customer_id, order_date) VALUES (4, '2024-07-04');

-- Tabelle für die eigentlichen Positionen (N:M) auf Produkte und Bestellungen anlegen
CREATE TABLE order_positions (
    order_id INT,
    product_id INT,
    anzahl INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

INSERT INTO order_positions (order_id, product_id, anzahl) VALUES (1, 1, 2); -- John Doe bestellt 2 Harley Davidson
INSERT INTO order_positions (order_id, product_id, anzahl) VALUES (1, 3, 1); -- John Doe bestellt 1 Titanic
INSERT INTO order_positions (order_id, product_id, anzahl) VALUES (2, 2, 1); -- Jane Smith bestellt 1 Boeing 747
INSERT INTO order_positions (order_id, product_id, anzahl) VALUES (3, 4, 1); -- Emily Jones bestellt 1 Ferrari
INSERT INTO order_positions (order_id, product_id, anzahl) VALUES (4, 4, 2); -- Michael Brown bestellt 2 Ferrari
