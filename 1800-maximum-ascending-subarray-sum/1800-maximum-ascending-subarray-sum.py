class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = nums[0]
        prev = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                prev = i
            answer = max(answer, sum(nums[prev:i+1]))
        return answer