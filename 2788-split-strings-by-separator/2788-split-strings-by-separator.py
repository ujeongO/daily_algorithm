class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            split_word_list = word.split(separator)
            for split_word in split_word_list:
                if split_word == "":
                    continue
                answer.append(split_word)
        return answer