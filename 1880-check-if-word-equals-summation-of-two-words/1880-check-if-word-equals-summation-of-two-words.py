class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(word):
            num_str = ""
            for c in word:
                num = ord(c) - 97
                num_str += str(num)
            return int(num_str)
        return convert(firstWord) + convert(secondWord) == convert(targetWord)