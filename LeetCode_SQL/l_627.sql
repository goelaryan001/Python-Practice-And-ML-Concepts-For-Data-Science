-- Write your PostgreSQL query statement below
Update Salary
SET sex= Case when sex='f' then 'm'
when sex='m' then 'f' end