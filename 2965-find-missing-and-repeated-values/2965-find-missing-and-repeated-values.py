from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        answer = [-1, -1]
        n = len(grid)
        c = Counter()
        for i in range(n):
            for j in range(n):
                c[grid[i][j]] += 1
        for i in range(1, n**2+1):
            if i not in list(c.keys()):
                answer[1] = i
            if c[i] == 2:
                answer[0] = i
        return answer