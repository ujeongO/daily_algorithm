class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        c = Counter(nums)
        k_freq = c.most_common()[:k]
        return [x[0] for x in k_freq]