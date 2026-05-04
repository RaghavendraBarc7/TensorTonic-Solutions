-- Write your SQL query here
SELECT department, 
       count(*) as total_tickets,
       sum(CASE
           WHEN status = 'open' THEN 1 
           ELSE 0
       END) as open_count, 
       sum(CASE
           WHEN status = 'in_progress' THEN 1 
           ELSE 0
       END) as in_progress_count,
       sum(CASE
           WHEN status = 'closed' THEN 1 
           ELSE 0
       END) as closed_count
from tickets
group by department 
order by total_tickets desc, department