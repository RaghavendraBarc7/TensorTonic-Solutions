-- Write your SQL query here
SELECT customer, count(*) as total_orders, sum(amount) as total_spent from orders
group by customer having count(*) >= 2
order by 3 desc