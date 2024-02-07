class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        answer = 0
        c1 = Counter(words1)
        c2 = Counter(words2)
        word_set = set(words1 + words2)
        for word in word_set:
            if c1[word] == 1 and c2[word] == 1:
                answer += 1
        return answer