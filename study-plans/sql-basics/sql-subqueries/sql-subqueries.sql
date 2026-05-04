-- Write your SQL query here
select a.name, a.price, a.price - (select avg(price) from products) as vs_avg from products a
where exists (select 1 from (select distinct product_id from sales) c where c.product_id = a.id)
order by vs_avg desc, name 
