-- Write your SQL query here
select u.username, e.experiment_name, e.variant, c.revenue from conversions c
left join users u on c.user_id = u.id
inner join experiment_assignments e on c.user_id = e.user_id
order by 2, 4 desc, 1