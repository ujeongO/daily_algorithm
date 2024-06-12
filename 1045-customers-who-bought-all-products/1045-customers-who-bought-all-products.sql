SELECT C.customer_id
FROM Customer AS C
GROUP BY C.customer_id
HAVING COUNT(*) = (SELECT COUNT(*) FROM Product)
