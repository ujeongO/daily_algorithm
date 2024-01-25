class Solution:
    def countAsterisks(self, s: str) -> int:
        answer = 0
        arr = s.split("|")
        for i in range(0, len(arr), 2):
            answer += arr[i].count('*')
        return answer