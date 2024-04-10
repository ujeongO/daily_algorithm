class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # 두 문자열 배열 word1과 word2가 동일한 문자열을 나타내면 참을 반환하고, 
        # 그렇지 않으면 거짓을 반환합니다.
        answer = True
        w1, w2 = '', ''
        for word in word1:
            w1 += word
        for word in word2:
            w2 += word
        if w1 != w2:
            answer = False
        return answer