class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cur_loc = 0         # 현재 위치
        visited = set()     # 폭탄을 가진 사람
        cnt = 1
        while cur_loc not in visited:
            visited.add(cur_loc)
            cur_loc = (cur_loc + (cnt * k)) % n
            cnt += 1
        return [x+1 for x in range(n) if x not in visited]