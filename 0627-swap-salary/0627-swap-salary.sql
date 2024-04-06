-- update문으로 작성
update
    Salary
set
    sex = if(sex="m", "f", "m")