class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(c) for c in str(n)]
        total_mul = 1
        total_sum = 0
        for num in nums:
            total_mul *= num
            total_sum += num
        return total_mul - total_sum