class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            word = word.split(separator)
            # answer.append(word)
            answer.extend(word)
        answer = [v for v in answer if v]
        return answer