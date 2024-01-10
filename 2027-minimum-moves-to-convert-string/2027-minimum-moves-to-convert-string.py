class Solution:
    def minimumMoves(self, s: str) -> int:
        answer = 0
        i = 0
        chart = [c for c in s]
        while i < len(chart):
            if chart[i] == 'X':
                answer += 1
                i += 3
            else:
                i += 1
        return answer