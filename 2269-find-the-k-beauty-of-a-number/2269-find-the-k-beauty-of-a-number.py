class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        answer = 0
        num_str = str(num)
        for i in range(len(num_str) - k + 1):
            substring_num = int(num_str[i:i+k])
            if substring_num == 0:
                continue
            if num % substring_num == 0:
                answer += 1
        return answer