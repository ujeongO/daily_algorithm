class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:    
        answer = sorted(nums)
        for i in range(0, len(nums), 2):
            answer[i], answer[i+1] = answer[i+1], answer[i]
        return answer