class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # 2중 for문을 enumerate rkxdl tkdyd
        answer = [-1, -1]
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if (abs(i-j) >= indexDifference) and abs(nums[i]-nums[j]) >= valueDifference:
                    answer = [i,j]
        return answer