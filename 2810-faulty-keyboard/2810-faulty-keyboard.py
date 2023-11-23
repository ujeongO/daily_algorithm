class Solution:
    def finalString(self, s: str) -> str:
        # 문자열 뒤집기
        # a = "hello"
        # b = a[::-1]
        # print(b)
        answer = ""
        for c in s:
            # i가 아니라면 그냥 answer에 더해주기
            if c != 'i':
                answer += c
            # i라면, 그동안 만든 문자열 뒤집기
            else:
                answer = answer[::-1]
        return answer