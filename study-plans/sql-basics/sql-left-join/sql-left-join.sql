-- Write your SQL query here
select c.name, c.city, coalesce(SUM(o.amount), 0) as total_spent from customers c 
left join orders o on c.id = o.customer_id
group by c.name, c.city
order by 3 desc, 1