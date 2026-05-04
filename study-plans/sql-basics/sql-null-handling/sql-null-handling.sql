-- Write your SQL query here
select name, if(email is null, 'N/A', email) as display_email, if(deactivated_at is null, 'active', 'inactive') as status
from customers
where phone is not null 
order by name