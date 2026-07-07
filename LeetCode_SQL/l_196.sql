-- Write your PostgreSQL query statement below
--Delete p2 from Person p1
--Join Person p2 on 
--p1.Email=p2.Email
--and
--p1.Id<p2.Id
--this above is for MYSQL as posgres doesnot support delete and join together it uses using

Delete from person p2
using Person p1
where
p1.Email=p2.Email
and
p1.Id<p2.Id