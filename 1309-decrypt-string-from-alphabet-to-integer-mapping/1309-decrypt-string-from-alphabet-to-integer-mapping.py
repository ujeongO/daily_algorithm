class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = ""
        num_dict = {}
        for i in range(26):
            c = chr(97 + i)
            if i >= 9:
                num_dict[str(i+1) + "#"] = c
            else:
                num_dict[str(i+1)] = c
        sorted_keys = sorted(list(num_dict.keys()), key=lambda x: (len(x), x), reverse=True)
        while s:
            for key in sorted_keys:
                if s.startswith(key):
                    s = s[len(key):]
                    answer += num_dict[key]
                    break
        return answer