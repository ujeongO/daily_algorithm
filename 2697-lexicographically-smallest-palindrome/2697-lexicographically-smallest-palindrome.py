class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        answer = ""
        mid = len(s) // 2
        for i in range(mid):
            selected = min(s[i], s[len(s) - i - 1])
            answer += selected
        if len(s) % 2:
            return answer + s[mid] + answer[::-1]
        else:
            return answer + answer[::-1]