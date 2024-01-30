class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for sentence in sentences:
            words = sentence.split(" ")
            answer = max(answer, len(words))
        return answer