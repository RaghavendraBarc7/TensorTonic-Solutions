-- Write your SQL query here
SELECT customer, count(distinct product) as total_orders, sum(amount) as total_spent from orders
group by customer 
order by 3 desc 