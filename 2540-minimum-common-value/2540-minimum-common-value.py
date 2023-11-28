class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums = set(nums1) & set(nums2)
        if len(nums) != 0:
            return min(nums)
        else:
            return -1