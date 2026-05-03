-- Write your SQL query here
select c.segment_name, m.metric_name from segments c
cross join metrics m 
order by c.segment_name, m.metric_name