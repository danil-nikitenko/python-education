create table if not exists address (
    address_id serial primary key,
    city varchar(255) not null,
    street varchar(255) not null,
    house_number int not null
);

create table if not exists branch (
    branch_id serial primary key,
    title varchar(255) not null,
    phone_number varchar(255),
    address_id int not null,
    foreign key(address_id) references address(address_id)
);

create table if not exists customer (
    customer_id serial primary key,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    phone_number varchar(255),
    address_id int not null,
    foreign key(address_id) references address(address_id)
);

create table if not exists car (
    car_id serial primary key,
    model varchar(255) not null,
    number varchar(255) not null,
    day_rental_price money not null,
    branch_id int not null ,
    foreign key(branch_id) references branch(branch_id)
);

create table if not exists rented (
    rented_id serial primary key,
    customer_id int not null,
    car_id int not null,
    rental_date timestamp(2) not null,
    rental_period_days int not null,
    to_pay money,
    foreign key(customer_id) references customer(customer_id),
    foreign key(car_id) references car(car_id)
);

-- address table filling
insert into address (
        city, street, house_number
        )
select
    'city ' || (floor(random() * (500-1+1) + 1))::text,
    ('street ' || floor(random() * (3000-1+1) + 1))::text,
    (floor(random() * (100-1+1) + 1))::int
from generate_series(1, 30000) s(i);

-- branch table filling
insert into branch (
        title, phone_number, address_id
        )
select
    'branch ' || i::text,
    (floor(random() * (9999999999-1234567890+1) + 1234567890))::text,
    i
from generate_series(1, 500) s(i);

-- customer table filling
insert into customer (
        first_name, last_name, phone_number, address_id
        )
select
    'first name ' || (floor(random() * (500-1+1) + 1))::text,
    'last name ' || (floor(random() * (10000-1+1) + 1))::text,
    (floor(random() * (9999999999-1234567890+1) + 1234567890))::text,
    i
from generate_series(501, 30000) s(i);

-- car table filling
insert into car (
        model, number, day_rental_price, branch_id
        )
select
    'model ' || (floor(random() * (500-1+1) + 1))::text,
    left(md5(i::text), 8),
    (floor(random() * (350-17+1) + 17))::int,
    (floor(random() * (500-1+1) + 1))::int
from generate_series(1, 50000) s(i);

-- rented table filling
insert into rented (
        customer_id, car_id, rental_date, rental_period_days
        )
select
    i,
    i,
    timestamp '2020-01-01 22:00:00' + random() * (timestamp '2021-12-31 22:00:00' - timestamp '2020-01-01 08:00:00'),
    (floor(random() * (30-1+1) + 1))::int
from generate_series(1, 29500) s(i);

update rented r set to_pay = (select day_rental_price from car c where c.car_id = r.car_id) * r.rental_period_days
where car_id between 1 and 29500;
