# 한 부서만 소속된 경우    -> 해당 부서만
# 여러 부서에 소속된 경우    -> primary_flag가 Y인 것만
# => 두 경우 union

-- 여러 부서에 소속된 경우
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = "Y"
UNION
-- 한 부서만 소속된 경우    -> 해당 부서만
SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(employee_id) = 1