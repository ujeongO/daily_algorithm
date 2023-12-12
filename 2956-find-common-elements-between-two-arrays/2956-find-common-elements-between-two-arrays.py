class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s_nums1, s_nums2 = set(nums1), set(nums2)
        cnt1, cnt2 = 0, 0
        for num in nums1:
            if num in s_nums2:
                cnt1 += 1
        for num in nums2:
            if num in s_nums1:
                cnt2 += 1
        return [cnt1, cnt2]