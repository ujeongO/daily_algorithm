class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = [0, 0]
        for num in nums1:
            if num in nums2:
                answer[0] += 1
        for num in nums2:
            if num in nums1:
                answer[1] += 1
        return answer