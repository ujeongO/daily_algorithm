class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            l_sum = sum(nums[:i])
            r_sum = sum(nums[i+1:])
            answer.append(abs(l_sum - r_sum))
        return answer