class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    answer += 1
        return answer