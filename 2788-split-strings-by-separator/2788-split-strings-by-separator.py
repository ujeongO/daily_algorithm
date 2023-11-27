class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            for i in word.split(separator):
                if i:
                    answer.append(i)
        return answer