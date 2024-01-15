class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = ""
        prev = ""
        cnt = 0
        for c in s:
            if c != prev:
                prev = c
                cnt = 1
            else:
                cnt += 1
            if cnt < 3:
                answer += c
        return answer