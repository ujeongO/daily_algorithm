-- 누락된 정보가 있는 모든 직원의 ID를 보고하는 솔루션을 작성하세요. 직원의 정보가 누락된 경우
-- 직원의 이름이 누락되었거나
-- 직원의 급여가 누락된 경우.
-- employee_id를 기준으로 오름차순으로 정렬된 결과 테이블을 반환합니다.
select
    E.employee_id
from
    Employees as E
left join
    Salaries as S
on 
    E.employee_id = S.employee_id
where
    S.salary is null 
union
select
    S.employee_id
from
    Employees as E
right join
    Salaries as S
on 
    E.employee_id = S.employee_id
where
    E.name is null
order by
    employee_id