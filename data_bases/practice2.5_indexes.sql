EXPLAIN ANALYSE SELECT * FROM users WHERE first_name = 'first_name 4000';
DROP INDEX users_first_name;
CREATE INDEX users_first_name ON users(first_name);

EXPLAIN ANALYSE SELECT * FROM products WHERE product_title = 'product 1'
                                          OR product_title = 'product 100'
                                          OR product_title = 'product 3900';
DROP INDEX products_product_title;
CREATE INDEX products_product_title ON products(product_title);

EXPLAIN ANALYSE SELECT COUNT(*) FROM products WHERE category_id = 11;
DROP INDEX products_category_id;
CREATE INDEX products_category_id ON products(category_id);
