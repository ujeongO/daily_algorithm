-- Company T의 name이 "RED"가 아닌 SalesPerson의 name 반환
-- 1. Company의 name이 "RED"인 S.name select
-- 2. SalesPerson T에서 1.의 결과 제외한 나머지 반환

SELECT S.name
FROM SalesPerson AS S
WHERE S.name NOT IN (SELECT S.name
                    FROM SalesPerson AS S
                    LEFT JOIN ORDERS AS O
                    ON S.sales_id = O.sales_id
                    LEFT JOIN Company AS C
                    ON O.com_id = C.com_id
                    WHERE C.name LIKE "RED")