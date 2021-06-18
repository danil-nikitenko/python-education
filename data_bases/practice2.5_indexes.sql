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

SET enable_seqscan TO OFF;

EXPLAIN ANALYSE SELECT
          p.product_title,
          p.product_description,
          p.price,
          c.category_title,
          o.order_id,
          o.created_at,
          os.status_name
FROM products p
INNER JOIN categories c USING(category_id)
INNER JOIN cart_product USING(product_id)
INNER JOIN orders o USING(cart_id)
INNER JOIN order_status os USING(order_status_id)
ORDER BY p.product_title;

DROP INDEX cart_product_product_id;
CREATE INDEX cart_product_product_id ON cart_product(product_id);
