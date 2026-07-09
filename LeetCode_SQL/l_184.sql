-- Write your PostgreSQL query statement below
with cte as
(select departmentId as Id, Max(salary)
from Employee 
group by departmentId)

select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e
inner join cte c
on e.departmentId=c.Id
and e.salary=c.max
join Department d
on e.departmentId=d.id