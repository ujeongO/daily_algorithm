class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        answer = 0
        for num in salary:
            if num == min_salary or num == max_salary:
                continue
            answer += num
        answer /= len(salary)-2
        return answer