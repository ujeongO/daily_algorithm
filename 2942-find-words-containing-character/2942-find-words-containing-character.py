class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer = []
        for i, word in enumerate(words):
            if x not in word:
                continue
            answer.append(i)
        return answer