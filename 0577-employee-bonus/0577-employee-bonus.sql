-- 상여금이 1000 미만인 각 직원의 이름과 상여금 반환
select
    E.name,
    B.bonus
from
    Employee as E
left join
    Bonus as B
on 
    E.empId = B.empId
where
    B.bonus < 1000
    or B.bonus is null