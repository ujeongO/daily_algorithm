class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                answer += len(set(nums[i:j])) ** 2
        return answer
