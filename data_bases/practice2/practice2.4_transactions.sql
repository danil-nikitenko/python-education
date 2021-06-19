-- potential_customers table
BEGIN;
INSERT INTO potential_customers (email, name, surname, second_name, city)
VALUES ('pc_email21@gmsil.com', 'name 21', 'surname 21', 'second name 21', 'city 21');
SAVEPOINT sp1;
INSERT INTO potential_customers (email, name, surname, second_name, city)
VALUES ('pc_email22@gmsil.com', '', '', '', 'city 22');
ROLLBACK TO SAVEPOINT sp1;
COMMIT;

BEGIN;
UPDATE potential_customers SET email = 'updated_email1@gamil.com' WHERE potential_customer_id = 1;
SAVEPOINT sp1;
UPDATE potential_customers SET email = 'pc_email5@gmail.com' WHERE potential_customer_id = 6;
ROLLBACK TO SAVEPOINT sp1;
COMMIT;

BEGIN;
SAVEPOINT sp1;
DELETE FROM potential_customers WHERE potential_customer_id = 21;
SAVEPOINT sp2;
DELETE FROM potential_customers WHERE potential_customer_id = 20;
SAVEPOINT sp3;
DELETE FROM potential_customers;
ROLLBACK TO SAVEPOINT sp3;
COMMIT;

-- users table
BEGIN;
INSERT INTO users (user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number)
VALUES (3001, 'email3001@gmail.com', '5728391932', 'first_name 3001', 'last_name 3001', 'middle_name 3001', 0, 'country 3001',
        'city 3001', 'address 3001', '');
SAVEPOINT sp1;
UPDATE users SET phone_number = '0332427893' WHERE user_id = 3001;
SAVEPOINT sp2;
DELETE FROM users WHERE user_id = 3001;
ROLLBACK TO SAVEPOINT sp2;
COMMIT;

--products table
BEGIN;
SAVEPOINT sp1;
INSERT INTO products (product_id, product_title, product_description, in_stock, price, slug, category_id)
VALUES (4001, 'Product 4001', 'Product description 4001', 16, 451.5, 'Product-4001', 13);
SAVEPOINT sp2;
INSERT INTO products (product_id, product_title, product_description, in_stock, price, slug, category_id)
VALUES (4002, 'Product 4002', 'Product description 4002', 31, 113.7, 'Product-4002', 4);
SAVEPOINT sp3;
INSERT INTO products (product_id, product_title, product_description, in_stock, price, slug, category_id)
VALUES (4003, 'Product 4003', 'Product description 4003', 7, 0, 'Product-4003', 9);
ROLLBACK TO SAVEPOINT sp3;
COMMIT;

BEGIN;
UPDATE products SET product_id = 9999999 WHERE product_id = 15;
UPDATE products SET in_stock = -25 WHERE product_id = 340;
DELETE FROM cart_product WHERE product_id BETWEEN 3000 AND 4000;
DELETE FROM products WHERE product_id BETWEEN 3000 AND 4000;
ROLLBACK;
