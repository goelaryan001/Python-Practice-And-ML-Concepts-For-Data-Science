select id,
case when p_id is null then 'ROOT'
when id in (select distinct p_id from tree where p_id is not null) then 'INNER'
else 'LEAF'
end as Type
from Tree
order by id