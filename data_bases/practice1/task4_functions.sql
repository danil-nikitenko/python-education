create or replace function rented_by_branch(b_id int)
returns table(
    rented_id int,
    rented_customer_id int,
    rented_car_id int,
    rented_rental_date date,
    rented_rental_period_days int
)
language plpgsql
as $$
begin
    return query
    select
           r.rented_id,
           r.customer_id,
           r.car_id,
           r.rental_date::date,
           r.rental_period_days
    from rented r
    join car using(car_id)
    join branch b using(branch_id)
    where b.branch_id = b_id;
end;$$;

select * from rented_by_branch(1);
drop function rented_by_branch(b_id int);

create or replace function get_not_rented_cars_from_branch(b_id int)
returns table(
    car_model varchar,
    car_day_rental_price money
)
language plpgsql
as $$
declare
    rec_car record;
    cur_cars cursor for
    select c.model, c.day_rental_price
    from car c
    left join rented r using(car_id)
    where r.car_id is null and c.branch_id = b_id
    order by c.day_rental_price;
begin
    open cur_cars;

    loop
        fetch cur_cars into rec_car;
        exit when not found;

        car_model := rec_car.model;
        car_day_rental_price := rec_car.day_rental_price;
        return next;
    end loop;
end;$$;

select * from get_not_rented_cars_from_branch(1);
drop function get_not_rented_cars_from_branch(b_id int);
