-- Write your PostgreSQL query statement below
Select c.name as Customers
From Customers c
Left Join Orders o
On c.id=o.customerId
where o.id IS NULL

Select c.name as Customers
From Customers c
where c.id NOT IN
(
Select c.id
From Customers c
Inner Join Orders o
On c.id=o.customerId
)