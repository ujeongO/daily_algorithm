-- 2. if) id%2==1 -> id+1
-- 3. if) id%2==0 -> id-1
-- 1. if) max(id) & id%2==1 -> 원래 id 반환

SELECT
    CASE
        WHEN id = (SELECT MAX(id) FROM Seat) AND id % 2 = 1 THEN id
        WHEN id % 2 = 1 THEN id + 1
        ELSE id - 1
    END AS id,
    student
FROM Seat
ORDER BY id