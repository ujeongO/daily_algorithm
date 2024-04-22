-- 아무것도 주문하지 않은 customer의 이름 반환

SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId
                FROM Orders)