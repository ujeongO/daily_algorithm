class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counterNums = Counter(nums)
        answer = []
        for key, value in counterNums.items():
            if value > len(nums) / 3:
                answer.append(key)
        return answer