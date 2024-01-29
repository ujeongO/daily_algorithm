class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0
        str_n = str(n)
        for i, num in enumerate(str_n):
            if i % 2:
                answer -= int(num)
            else:
                answer += int(num)
        return answer