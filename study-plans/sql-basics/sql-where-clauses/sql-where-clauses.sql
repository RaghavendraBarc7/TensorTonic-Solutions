-- Write your SQL query here
SELECT name, salary from employees
where department IN ('Engineering', 'Marketing') and salary > 70000