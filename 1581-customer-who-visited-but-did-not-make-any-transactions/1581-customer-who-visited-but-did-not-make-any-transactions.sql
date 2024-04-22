-- 거래를 하지 않고 방문한 사용자의 ID, 방문 횟수 리턴 -> 차집합 이용
-- customer_id -> 30, 96, 54

SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM Visits AS V
LEFT JOIN Transactions AS T
ON V.visit_id = T.visit_id
WHERE T.visit_id IS NULL
GROUP BY customer_id