-- 삼각형을 만들어보자!
-- 조건) 두 변의 합이 나머지 한 변의 길이보다 길어야 함.
SELECT *,
    if(((x+y)>z and (y+z)>x and (x+z)>y), "Yes", "No") AS triangle
FROM
    triangle