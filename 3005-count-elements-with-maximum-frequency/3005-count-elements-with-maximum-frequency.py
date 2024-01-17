class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        answer = 0
        c = Counter(nums)
        max_value = max(c.values())
        for k,v in c.items():
            if v == max_value:
                answer += v
        return answer