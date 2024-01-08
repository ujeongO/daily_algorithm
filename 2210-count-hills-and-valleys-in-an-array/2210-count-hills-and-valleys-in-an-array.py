class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        answer = 0
        new_nums = [nums[0]]
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev:
                new_nums.append(nums[i])
                prev = nums[i]
        for i in range(1, len(new_nums)-1):
            if new_nums[i] > new_nums[i-1] and new_nums[i] > new_nums[i+1]:
                answer += 1
            if new_nums[i] < new_nums[i-1] and new_nums[i] < new_nums[i+1]:
                answer += 1
        return answer