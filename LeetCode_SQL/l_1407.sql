with cte as
(select user_id, sum(distance) as travelled_distance
from rides
group by uder_id)

select u.name, case when cte.travelled_distance is null then 0 else cte.travelled_distance end
from Users u
left join cte
on u.id=cte.user_id
order by
case when cte.travelled_distance is null then 0 else cte.trvlled_distance end desc, u.name