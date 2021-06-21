create or replace procedure rent_car(customer_id int, car_id int, period int)
language plpgsql
as $$
begin
       insert into rented (customer_id, car_id, rental_date, rental_period_days) values($1, $2, now(), $3);
       if (select count(r.car_id) from rented r where r.car_id = $2) > 1 then
           rollback;
        else
           update rented r set to_pay = (select day_rental_price from car c where c.car_id = $2) * $3
           where r.car_id = $2;
       end if;
       commit;
end;$$;

begin;
call rent_car(1, 30000, 5);
rollback;

drop procedure rent_car(customer_id int, car_id int, period int);

create or replace procedure write_off_car(car_id int)
language plpgsql
as $$
begin
    if exists (select r.car_id from rented r where r.car_id = $1) then
        raise 'Car with id % is rented', $1;
    else
        delete from car c where c.car_id = $1;
    end if;
end;$$;

begin;
call write_off_car(30000);
rollback;

drop procedure write_off_car(car_id int);
