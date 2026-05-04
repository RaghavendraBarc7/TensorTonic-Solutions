-- Write your SQL query here
select round(sum(cnt)/count(order_date), 2) as avg_daily_orders, round(sum(summ)/count(order_date), 2) as avg_daily_revenue, max(cnt) as busiest_day_orders from 
(select order_date, count(*) as cnt, sum(amount) as summ from orders 
group by order_date) a 