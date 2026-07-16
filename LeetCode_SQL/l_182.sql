-- Write your PostgreSQL query statement below
Select email as Email
from Person
Group by email 
having count(distinct id)>1

SELECT DISTINCT email AS Email
FROM (
    SELECT
        email,
        COUNT(*) OVER (PARTITION BY email) AS cnt
    FROM Person
) t
WHERE cnt > 1;