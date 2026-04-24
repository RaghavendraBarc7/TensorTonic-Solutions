-- Write your SQL query here
select customer_name, count(distinct product) as unique_products from orders
group by customer_name
order by 2 desc, 1