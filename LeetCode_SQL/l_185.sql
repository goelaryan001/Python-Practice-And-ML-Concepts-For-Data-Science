-- Write your PostgreSQL query statement below
with cte as(select e.name as EmployeeName, e.salary as Salary, d.name as DepartmentName      -- joe 85000 IT
from Employee e                       -- Henry 80000 Sales
inner join Department d
on e.departmentId=d.id),
cte2 as
(select EmployeeName, Salary, DepartmentName,
dense_rank() over(partition by DepartmentName order by Salary desc) as rnk
from cte )
select DepartmentName as Department, EmployeeName as Employee, Salary
from cte2 
where
rnk<=3