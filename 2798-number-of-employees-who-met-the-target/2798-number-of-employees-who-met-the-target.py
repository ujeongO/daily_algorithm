class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # target 이상인 수 count
        answer = 0
        for hour in hours:
            if hour < target:
                continue
            answer += 1
        return answer