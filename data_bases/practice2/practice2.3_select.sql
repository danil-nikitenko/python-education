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
SELECT p.product_id
FROM products p
    LEFT JOIN cart_product cp USING(product_id)
WHERE cp.product_id IS NULL;
-- № 2
SELECT p.product_id
FROM products p
    FULL JOIN cart_product cp USING (product_id)
    LEFT JOIN orders o USING (cart_id)
WHERE o.cart_id IS NULL
GROUP BY p.product_id
ORDER BY p.product_id DESC;
-- № 3
SELECT p.product_id, COUNT(cp.cart_id)
FROM products p
    JOIN cart_product cp USING(product_id)
GROUP BY p.product_id ORDER BY count DESC LIMIT 10;
-- № 4
SELECT p.product_id, COUNT(cp.cart_id)
FROM products p
    JOIN cart_product cp USING(product_id)
    JOIN orders o USING(cart_id)
GROUP BY p.product_id ORDER BY count DESC LIMIT 10;
-- № 5
SELECT u.user_id, SUM(c.total)
FROM users u
    JOIN carts c USING(user_id)
    JOIN orders o USING(cart_id)
GROUP BY u.user_id ORDER BY sum DESC LIMIT 5;
-- № 6
SELECT u.user_id, COUNT(c.cart_id)
FROM users u
    JOIN carts c USING(user_id)
    JOIN orders o USING(cart_id)
GROUP BY u.user_id ORDER BY count DESC LIMIT 5;
-- № 7
SELECT u.user_id
FROM users u
    INNER JOIN carts c USING(user_id)
    LEFT JOIN orders o USING(cart_id)
WHERE o.cart_id IS NULL
ORDER BY u.user_id DESC LIMIT 5;
