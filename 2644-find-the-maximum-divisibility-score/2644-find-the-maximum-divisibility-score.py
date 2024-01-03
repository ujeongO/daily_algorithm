class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        answer = (-1, -1)
        divisors.sort()
        for divisor in divisors:
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            if answer[1] < score:
                answer = (divisor, score)
        return answer[0]