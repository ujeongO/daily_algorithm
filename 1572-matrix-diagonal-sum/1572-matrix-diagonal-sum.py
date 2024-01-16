class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        n = len(mat)
        for i in range(n):
            answer += mat[i][i]
            answer += mat[i][n-i-1]
        if n % 2 == 1:
            mid = n // 2
            answer -= mat[mid][mid]
        return answer