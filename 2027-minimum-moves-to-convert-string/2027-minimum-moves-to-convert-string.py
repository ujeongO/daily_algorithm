class Solution:
    def minimumMoves(self, s: str) -> int:
        answer = 0
        chars = [c for c in s]
        for i, c in enumerate(chars):
            if c == 'X':
                chars[i] = "O"
                if i < len(s) - 1:
                    chars[i+1] = "O"
                if i < len(s) - 2:
                    chars[i+2] = "O"
                answer += 1
        return answer