-- TASK 1
CREATE TABLE IF NOT EXISTS  potential_customers (
    potential_customer_id serial primary key ,
    email varchar(255),
    name varchar(255),
    surname varchar(255),
    second_name varchar(255),
    city varchar(255)
);

SELECT first_name, email FROM users WHERE city = 'city 17'
UNION SELECT name, email FROM potential_customers WHERE city = 'city 17';

-- TASK 2
SELECT city, first_name, email FROM users
ORDER BY city, first_name;

-- TASK 3
SELECT c.category_title, COUNT(p.category_id) total_products FROM products p
INNER JOIN categories c USING(category_id)
GROUP BY c.category_title
ORDER BY total_products DESC;

--TASK 4
-- № 1
SELECT * FROM products WHERE product_id NOT IN (SELECT product_id FROM cart_product);
-- № 2
SELECT * FROM products WHERE product_id NOT IN (
    SELECT product_id FROM cart_product WHERE cart_id IN (
        SELECT cart_id FROM carts WHERE cart_id IN (SELECT cart_id FROM orders)
        )
    );
-- № 3
CREATE OR REPLACE VIEW top_ten_products_in_carts AS
SELECT product_id, COUNT(cart_id) total FROM cart_product GROUP BY product_id ORDER BY total DESC LIMIT 10;

SELECT * FROM products WHERE product_id IN (SELECT product_id FROM top_ten_products_in_carts);
-- № 4
CREATE OR REPLACE VIEW top_ten_products_in_orders AS
SELECT product_id, COUNT(cart_id) total FROM cart_product WHERE cart_id IN (
    SELECT cart_id FROM carts WHERE cart_id IN (SELECT cart_id FROM orders)
    )GROUP BY product_id ORDER BY total DESC LIMIT 10;

SELECT * FROM products WHERE product_id IN ( SELECT product_id FROM top_ten_products_in_orders);
-- № 5
CREATE OR REPLACE VIEW top_five_user_with_the_most_money_spent AS
SELECT user_id, SUM(total) FROM carts WHERE cart_id IN (
    SELECT cart_id FROM carts WHERE cart_id IN (SELECT cart_id FROM orders)
    )GROUP BY user_id ORDER BY sum DESC LIMIT 5;

SELECT * FROM users WHERE user_id IN (SELECT user_id FROM top_five_user_with_most_money_spent);
-- № 6
CREATE OR REPLACE VIEW top_five_user_with_the_largest_number_of_orders AS
SELECT user_id, COUNT(cart_id) FROM carts WHERE cart_id IN (
    SELECT cart_id FROM carts WHERE cart_id IN (SELECT cart_id FROM orders)
    ) GROUP BY user_id ORDER BY count DESC LIMIT 5;

SELECT * FROM users WHERE user_id IN (SELECT user_id FROM top_five_user_with_the_largest_number_of_orders);
-- № 7
SELECT * FROM users WHERE user_id NOT IN (
    SELECT user_id FROM carts WHERE cart_id IN (SELECT cart_id FROM orders)
    ) ORDER BY user_id LIMIT 5;
