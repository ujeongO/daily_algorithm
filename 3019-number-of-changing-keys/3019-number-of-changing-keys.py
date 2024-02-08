class Solution:
    def countKeyChanges(self, s: str) -> int:
        answer = 0
        s = s.lower()
        prev = s[0]
        for c in s:
            if c != prev:
                answer += 1
            prev = c
        return answer