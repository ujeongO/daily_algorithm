class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter

        counter_s = Counter(s)
        counter_t = Counter(t)
        return list((counter_t - counter_s).keys())[0]