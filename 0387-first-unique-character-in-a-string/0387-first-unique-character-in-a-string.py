class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = -1
        c = Counter(s)
        for k, v in c.items():
            if v == 1:
                answer = s.index(k)
                return answer
        return answer