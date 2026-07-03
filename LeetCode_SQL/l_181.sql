-- Write your PostgreSQL query statement below
Select e1.name as Employee
From Employee e1
Inner Join Employee e2
ON e1.managerId=e2.Id
where e1.salary>e2.salary