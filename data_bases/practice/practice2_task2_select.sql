-- TASK 2.1
-- № 1
SELECT * FROM users;
-- № 2
SELECT * FROM products;
-- № 3
SELECT * FROM order_status;

-- TASK 2.2
SELECT * FROM orders WHERE order_status_id = 4;

-- TASK 2.3
-- № 1
SELECT * FROM products WHERE price > 80.0 AND price <= 150.0;
SELECT * FROM products WHERE price BETWEEN 80.0 AND 150.0;
-- № 2
SELECT * FROM orders WHERE created_at::timestamp > date '2020-10-01';
-- № 3
SELECT * FROM orders WHERE created_at::timestamp > date '2020-01-01' AND created_at::timestamp <= date '2020-06-30';
SELECT * FROM orders WHERE created_at::timestamp BETWEEN date '2020-01-01' AND date '2020-06-30';
-- № 4
SELECT * FROM products WHERE category_id = 7 OR category_id = 11 OR category_id = 18;
SELECT * FROM products WHERE category_id IN (7, 11, 18);
SELECT * FROM products WHERE category_id IN (
    SELECT category_id FROM categories
    WHERE category_title IN ('Category 7', 'Category 11', 'Category 18')
    );
-- № 5
SELECT * FROM orders WHERE order_status_id = 2 AND updated_at::timestamp = date '2020-12-31';
-- № 6
SELECT * FROM carts WHERE cart_id IN (SELECT cart_id FROM orders WHERE order_status_id = 5);

-- TASK 2.4
-- № 1
SELECT avg(total)average_sum FROM orders WHERE order_status_id = 4;
-- № 2
SELECT max(total)max_sum FROM orders WHERE created_at::timestamp BETWEEN date '2020-07-01' AND date '2020-09-30';
