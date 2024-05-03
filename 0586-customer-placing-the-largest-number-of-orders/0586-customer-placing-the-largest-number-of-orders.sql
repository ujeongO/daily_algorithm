-- 가장 많은 주문을 한 고객의 고객 번호 출력
-- 정확히 한 명의 고객이 다른 고객보다 더 많은 주문을 하도록 테스트 케이스가 생성됩니다.

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1