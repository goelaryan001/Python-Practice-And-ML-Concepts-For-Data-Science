select case when u.unique_id is null then null else u.unique_id end, e.name
from Employees e
left join EmployeeUNI u
on e.id=u.id