-- Write your PostgreSQL query statement below
with cte as
(select num
from MyNumbers
Group By num
Having Count(num)=1)

select Case when count(*)>0 Then Max(num) 
else NULL end as num
from cte