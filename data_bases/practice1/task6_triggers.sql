create or replace function update_rented_to_pay()
returns trigger
language plpgsql
as $$
begin
    update rented
    set to_pay = (select day_rental_price from car where car_id = new.car_id) * new.rental_period_days
    where rented_id = new.rented_id;
    return new;
end;$$;

create trigger rented_after_insert_or_update
    after insert or update of car_id, rental_period_days
    on rented
    for each row
    execute procedure update_rented_to_pay();

begin;
insert into rented (customer_id, car_id, rental_date, rental_period_days) values (1, 30000, now(), 5);
update rented set car_id = 35000 where rented_id = 1;
update rented set rental_period_days = 15 where rented_id = 1;
rollback;

drop trigger rented_after_insert_or_update on rented;
drop function update_rented_to_pay();

create or replace function delete_branch()
returns trigger
language plpgsql
as $$
begin
    delete from rented where car_id in (select car_id from car where branch_id = old.branch_id);
    delete from car where branch_id = old.branch_id;
    return old;
end;$$;

create trigger branch_before_delete
    before delete
    on branch
    for each row
    execute procedure delete_branch();

begin;
delete from branch where branch_id = 2;
rollback;

drop trigger branch_before_delete on branch;
drop function delete_branch();
