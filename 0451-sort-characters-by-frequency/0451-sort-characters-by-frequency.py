class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        sorted_s = sorted(s, key=lambda x: (-c[x], x))
        return "".join(sorted_s)