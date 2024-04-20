-- 2020년 2월에 100개 이상 주문된 제품의 이름과 수량 반환
SELECT P.product_name, SUM(O.unit) AS unit
FROM Products AS P
LEFT JOIN Orders AS O
ON P.product_id = O.product_id
WHERE YEAR(O.order_date) = 2020 AND MONTH(O.order_date) = 2
GROUP BY P.product_name
HAVING SUM(O.unit) >= 100