with cte as
(select managerID, count(id) as qty
from Employee
where managerId is not null
group by managerId)

select e.name
from cte
inner join Employee e
on cte.managerId=cte.id
where cte.qty>=5