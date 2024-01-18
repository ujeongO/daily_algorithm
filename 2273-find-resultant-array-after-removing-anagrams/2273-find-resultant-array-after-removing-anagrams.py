class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        answer = []
        prev = ""
        for word in words:
            sorted_prev = ''.join(sorted(prev))
            sorted_word = ''.join(sorted(word))
            if sorted_prev == sorted_word:
                continue
            else:
                answer.append(word)
            prev = word
        return answer