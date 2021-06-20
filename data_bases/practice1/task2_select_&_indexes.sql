SET enable_seqscan TO OFF;

drop index rented_car_id;
create index rented_car_id on rented(car_id);
-- branches with most cars rented
explain analyse select b.branch_id, b.title, count(r.car_id) cars_rented
from branch b
join car c using(branch_id)
join rented r using(car_id)
group by b.branch_id
order by cars_rented desc
limit 10;

drop index rented_car_id;
create index rented_car_id on rented(car_id);
-- not rented cars
explain analyse select c.car_id, c.model
from car c
left join rented r using(car_id)
where r.car_id is null;

SET enable_seqscan TO ON;

drop index rented_customer_id;
create index rented_customer_id on rented(customer_id);
drop index customer_address_id;
create index customer_address_id on customer(address_id);
drop index address_city;
create index address_city on address(city);
-- cars rented by customers from city 17 for a period from 1 to 7 days
explain analyse select c.car_id, c.model, c.number, b.title branch
from car c
join rented r using(car_id)
join customer using(customer_id)
join address a using(address_id)
join branch b using(branch_id)
where a.city = 'city 17' and r.rental_period_days between 1 and 7
order by b.title;
