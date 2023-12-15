class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        answer = 0
        max_num = max(nums)
        for i in range(k):
            answer += (max_num + i)
        return answer