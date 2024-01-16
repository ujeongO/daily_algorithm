from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        sorted_nums = sorted(nums, key=lambda x: (c[x], -x))
        return sorted_nums