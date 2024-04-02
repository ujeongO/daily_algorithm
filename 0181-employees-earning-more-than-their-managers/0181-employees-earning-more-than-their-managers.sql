select
    em1.name as Employee
    -- em1.id, em1.name, em2.name
from 
    Employee as em1
join 
    Employee as em2
on
    em1.managerId = em2.id
where
    em1.salary > em2.salary