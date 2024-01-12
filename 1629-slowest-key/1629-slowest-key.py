from collections import defaultdict

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        d = defaultdict(int)
        prev = 0
        for i, time in enumerate(releaseTimes):
            duration = time - prev
            prev = time
            d[keysPressed[i]] = max(d[keysPressed[i]], duration)
        answer = ""
        cur_max = 0
        for k, v in d.items():
            if v > cur_max:
                answer = k
                cur_max = v
            elif v == cur_max and answer < k:
                answer = k
        return answer