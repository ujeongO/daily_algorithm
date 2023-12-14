class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cur_loc = 0
        visited = set()
        visited.add(cur_loc)
        cnt = 0
        while True:
            cnt += 1
            next_loc = (cur_loc + cnt*k) % n
            if next_loc in visited:
                break
            cur_loc = next_loc
            visited.add(cur_loc)
        return [x+1 for x in range(n) if x not in visited]
        