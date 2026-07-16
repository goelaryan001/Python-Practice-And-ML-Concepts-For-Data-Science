select w1.id
from Weather w1
join Weather w2
on w1.recordDate=w2.recordDate + Interval '1 day'
where w1.temperature>w2.temperature

with cte as
(select
id,
temperature,
recordDate,
LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date,
lag(temperature) over (order by recordDate) as prev
from Weather) 

select id from cte
where temperature > prev
and recordDate=prev_date+interval '1 day'
