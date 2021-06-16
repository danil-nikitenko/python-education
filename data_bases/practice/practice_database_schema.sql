CREATE TABLE IF NOT EXISTS users (
    user_id serial,
    email varchar(255),
    password varchar(255),
    first_name varchar(255),
    last_name varchar(255),
    middle_name varchar(255),
    is_staff smallint ,
    country varchar(255),
    city varchar(255),
    address text,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS order_status (
    order_status_id serial,
    status_name varchar(255),
    PRIMARY KEY (order_status_id)
);

CREATE TABLE IF NOT EXISTS categories (
    category_id serial,
    category_title varchar(255),
    category_description text,
    PRIMARY KEY (category_id)
);

CREATE TABLE IF NOT EXISTS products (
    product_id serial,
    product_title varchar(255),
    product_description text,
    in_stock int,
    price float,
    slug varchar(45),
    category_id int,
    PRIMARY KEY (product_id),
    FOREIGN KEY (category_id) REFERENCES categories (category_id)
);

CREATE TABLE IF NOT EXISTS carts (
    cart_id serial,
    user_id int,
    subtotal decimal,
    total decimal,
    timestamp timestamp(2),
    PRIMARY KEY (cart_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE IF NOT EXISTS cart_product (
    cart_id int,
    product_id int,
    FOREIGN KEY (cart_id) REFERENCES carts (cart_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id),
    PRIMARY KEY (cart_id, product_id)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id serial,
    cart_id int,
    order_status_id int,
    shipping_total decimal,
    total decimal,
    created_at timestamp(2),
    updated_at timestamp(2),
    PRIMARY KEY (order_id),
    FOREIGN KEY (cart_id) REFERENCES carts (cart_id),
    FOREIGN KEY (order_status_id) REFERENCES order_status (order_status_id)
);
