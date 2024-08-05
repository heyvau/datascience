CREATE DATABASE online_shop;

CREATE TABLE customer(
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    address VARCHAR(200)
);

INSERT INTO customer(first_name, last_name, email, address)
VALUES
    ("Jack", "Black", "jblack@email.hi", "Welcomestr. 1, 01234 Hallo"),
    ("Tony", "Looney", "tlooney@email.hi", "Sunnystr. 32, 04321 Nightcity");

SELECT * FROM customer;

CREATE TABLE customer_order(
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATE,
    status BOOLEAN,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

INSERT INTO customer_order(order_date, status, customer_id)
VALUES
    ("2024-06-30", 1, 1),
    ("2024-07-20", 0, 1),
    ("2024-07-22", 0, 2);

SELECT * FROM customer_order WHERE customer_id = 1;

CREATE TABLE product(
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    description TEXT,
    preis DECIMAL(10, 2)
);

INSERT INTO product(name, description, preis)
VALUES
    ("Whiskas", "Food for cats", 23.90),
    ("Elmex", "Toothpaste", 4.79),
    ("Volvic", "Mineral water, 1.5 l", 0.95),
    ("Albi", "Fruit juice, 1 l", 2.10),
    ("Melitta", "Coffee, 500 g", 8.99),
    ("Ben & Jerry's", "Ice cream, 200 g", 6.49);

SELECT * FROM product;

CREATE TABLE order_position(
    position_id INT PRIMARY KEY AUTO_INCREMENT,
    amount INT,
    total_preis DECIMAL(10, 2),
    order_id INT,
    product_id INT,
    UNIQUE (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES customer_order(order_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

INSERT INTO order_position(amount, order_id, product_id)
VALUES
    (2, 1, 5),
    (4, 1, 3),
    (1, 1, 6),
    (1, 2, 2),
    (4, 2, 1),
    (6, 3, 4),
    (2, 3, 3),
    (4, 3, 6),
    (3, 3, 2);

-- INSERT INTO order_position(amount, order_id, product_id)
-- VALUES
--     (1, 3, 2);

UPDATE order_position AS op
INNER JOIN product AS p
ON p.product_id = op.product_id
SET op.total_preis = op.amount * p.preis;

SELECT product.name, product.preis, order_position.amount, order_position.total_preis
FROM product 
INNER JOIN order_position
ON product.product_id = order_position.product_id
WHERE order_position.order_id = 3;
