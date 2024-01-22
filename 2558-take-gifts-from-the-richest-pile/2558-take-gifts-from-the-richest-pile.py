class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts = sorted(gifts)
            max_gift = gifts.pop()
            gifts.append(int(sqrt(max_gift)))
        return sum(gifts)