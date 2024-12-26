CREATE DATABASE ecommerce;

\c ecommerce;

CREATE TABLE transactions (
    user_id INT,
    product_id INT,
    price INT,
    timestamp TIMESTAMP
);
