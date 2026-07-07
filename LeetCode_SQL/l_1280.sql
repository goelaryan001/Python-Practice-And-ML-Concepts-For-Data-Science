-- Write your PostgreSQL query statement below
with cte as
(select *
from Students                --1 Alice Math
cross join Subjects),         --1 Alice Physics

cte2 as
(Select student_id, subject_name, count(subject_name) as cnt --1. Math  3
from Examinations
group by student_id, subject_name)

select cte.student_id, cte.student_name, cte.subject_name, case when cnt is not null then cnt else 0 end as attended_exams
from cte 
left join cte2
on cte.student_id=cte2.student_id
and cte.subject_name=cte2.subject_name
order by cte.student_id,cte.subject_name