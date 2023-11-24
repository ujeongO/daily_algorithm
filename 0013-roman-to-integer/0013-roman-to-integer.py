class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        keys = sorted(d.keys(), reverse=True)
        answer = 0
        while s:
            for key in keys:
                if s.startswith(key):
                    answer += d[key]
                    s = s[len(key):]
                    break
        return answer