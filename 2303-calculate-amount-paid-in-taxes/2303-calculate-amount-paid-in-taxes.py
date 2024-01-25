class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = prev = 0
        for upper, percent in brackets:
            if income >= upper:
                amount = upper - prev
                answer += amount * percent * 0.01
                prev = upper
            else:
                amount = income - prev
                answer += amount * percent * 0.01
                break
        return answer