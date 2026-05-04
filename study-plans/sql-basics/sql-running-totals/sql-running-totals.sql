-- Write your SQL query here
select account, txn_date, amount, sum(amount) over (partition by account ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) as running_total 
from transactions 
order by account, txn_date, id