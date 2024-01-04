class Solution:
    def minMaxDifference(self, num: int) -> int:
        candidates = []
        for i in range(10):
            candidates.append(int(str(num).replace(str(i), "9")))
            candidates.append(int(str(num).replace(str(i), "0")))
        return max(candidates) - min(candidates)