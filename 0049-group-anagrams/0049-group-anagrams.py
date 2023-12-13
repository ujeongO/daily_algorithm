from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary
        # key: 알파벳 순으로 정렬한 문자열
        # value: 해당하는 문자 리스트
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        print(d.values())
        return list(d.values())