-- Write your PostgreSQL query statement below
Select email as Email
from Person
Group by email 
having count(distinct id)>1