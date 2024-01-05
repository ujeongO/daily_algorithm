class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        answer = -1
        for i in range(len(nums)):
            l_side = nums[:i]
            r_side = nums[i+1:]
            if sum(l_side) == sum(r_side):
                return i
        return answer