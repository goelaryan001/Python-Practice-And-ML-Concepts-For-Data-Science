-- Write your PostgreSQL query statement below
Select Max(Salary) as SecondHighestSalary
From Employee
Where Salary Not in (Select Max(Salary) from Employee)
Limit 1
