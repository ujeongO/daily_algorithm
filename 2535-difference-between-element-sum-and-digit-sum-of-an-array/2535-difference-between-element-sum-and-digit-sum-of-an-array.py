class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            for c in str(num):
                digit_sum += int(c)
        return abs(element_sum - digit_sum)