from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        c = Counter(nums)
        for k, v in c.items():
            if v % 2 != 0:
                return False
        return True

        