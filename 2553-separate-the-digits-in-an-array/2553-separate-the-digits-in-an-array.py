class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            for c in str(num):
                answer.append(int(c))
        return answer