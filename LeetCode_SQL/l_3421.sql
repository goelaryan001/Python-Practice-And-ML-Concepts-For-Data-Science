-- Write your PostgreSQL query statement below
with cte as(select
s.student_id,
s.subject,
s.score,
s.exam_date,
row_number() over(partition by s.student_id, s.subject order by exam_date asc) rn1
from Scores s),
cte2 as
( select
t.student_id,
t.subject,
t.score,
t.exam_date,
row_number() over(partition by t.student_id, t.subject order by exam_date desc) as rn2
from Scores t
)
select 
c1.student_id,
c1.subject,
c1.score as first_score,
c2.score as latest_score
from cte as c1
inner join cte2 as c2
on c1.student_id=c2.student_id and c1.subject=c2.subject
where 
c1.rn1 = 1
and c2.rn2 = 1
and c1.score<c2.score