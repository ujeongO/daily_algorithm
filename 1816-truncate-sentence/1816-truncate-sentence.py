class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        answer = ""
        list_s = s.split(" ")
        list_s = list_s[:k]
        answer = ' '.join(list_s)
        return answer