class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        answer = ""
        mid = len(s) // 2
        for i in range(mid):
            # 두 알파벳 비교, 알파벳 순서상 더 작은 거 선택
            selected = min(s[i], s[len(s) - i - 1])
            answer += selected
        # s 길이가 홀수일 때: mid 더해주기
        if len(s) % 2:
            return answer + s[mid] + answer[::-1]
        # s 길이가 짝수일 때: answer에 뒤집은 거 더해주기
        else:
            return answer + answer[::-1]