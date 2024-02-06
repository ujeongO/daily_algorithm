class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        location = 0
        answer = 0
        for num in nums:
            location += num
            if location == 0:
                answer += 1
        return answer