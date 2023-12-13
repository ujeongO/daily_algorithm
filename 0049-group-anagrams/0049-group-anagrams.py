from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict 정렬 -> 비교
        # key가 같은 것들 하나로 묶음
        answer = []
        ana = collections.defaultdict(list)
        for string in strs:
            c_string = Counter(string)
            l_string = list(c_string.items())
            l_string = sorted(l_string)
            # print(l_string)
            ana[tuple(l_string)].append(string)
            # print(ana)
        # print(ana.items())
        for k, v in ana.items():
            answer.append(v)
        return answer