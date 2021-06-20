create or replace view not_rented_cars
as select
c.car_id,
c.branch_id
from car c
left join rented r using(car_id)
where r.car_id is null;

select * from not_rented_cars;
drop view not_rented_cars;

create or replace view top_5_rented_cars_by_price
as select
c.car_id,
r.rental_period_days,
c.day_rental_price * r.rental_period_days as total_price
from car c
join rented r using(car_id)
order by total_price desc
limit 5;

select * from top_5_rented_cars_by_price;
drop view top_5_rented_cars_by_price;

create materialized view top_5_branches_with_most_customers
as select
b.branch_id,
count(customer.customer_id) as customers,
sum(car.day_rental_price * r.rental_period_days) as gain
from branch b
join car using(branch_id)
join rented r using(car_id)
join customer using(customer_id)
group by b.branch_id
order by customers desc
limit 5;

select * from top_5_branches_with_most_customers;
drop materialized view top_5_branches_with_most_customers;
