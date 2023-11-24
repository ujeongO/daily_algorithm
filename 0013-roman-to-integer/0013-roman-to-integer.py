class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        sym = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if sym[s[i]] < sym[s[i+1]]:
                answer -= sym[s[i]]
                continue
            answer += sym[s[i]]
        return answer + sym[s[-1]]