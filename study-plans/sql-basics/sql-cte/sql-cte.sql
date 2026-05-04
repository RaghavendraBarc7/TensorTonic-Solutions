-- Write your SQL query here
select customer, count(distinct order_date) as order_count, sum(amount) as total_spent
from orders 
group by customer having count(distinct order_date) > 1
order by 3 desc, 1