class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        answer = float('inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        answer = min(answer, (nums[i]+nums[j]+nums[k]))
        return answer if answer!=float('inf') else -1