-- Write your PostgreSQL query statement below
with cte as 
(select *,
id - ROW_NUMBER() OVER (ORDER BY id) AS grp
from Stadium
where people>=100),
good_groups AS (
select grp
from cte
group by grp
having count(*) >= 3
)
SELECT
id,
visit_date,
people
from cte
where grp in (select grp from good_groups)
order by visit_date


-- 2 xx 109 1
-- 3 xx 150 1
-- 5 xx 145 2
-- 6 xx 1455 2
-- 7 xx 199 2
-- 8 xx 188 2