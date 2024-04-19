-- 중복된 이메일 반환
SELECT
    email as Email
FROM
    Person
GROUP BY
    email
HAVING
    COUNT(Id) > 1