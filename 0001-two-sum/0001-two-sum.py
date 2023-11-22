class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        isCorrect = False
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    isCorrect = True
                    return [i,j]
                    break
            # if isCorrect:
            #     break