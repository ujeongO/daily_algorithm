class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        sorted_arr = sorted(arr, key=lambda x: int(x[-1]))
        return " ".join(x[:-1] for x in sorted_arr)