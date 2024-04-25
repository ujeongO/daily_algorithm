-- 1000에서 weight를 빼다가
-- 뺀 값이 0보다 작거나 같으면
-- -> weight를 누적해서 더하기
-- 마지막 이름 반환 => 내림차순 정렬 -> 첫 번째 행
SELECT person_name
FROM
    (SELECT *, SUM(weight) OVER (ORDER BY turn) AS Total
    FROM Queue) p1
WHERE Total <= 1000
ORDER BY turn DESC
LIMIT 1