class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        from collections import Counter
        
        answer = []
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)
        set_all = Counter(list(set1) + list(set2) + list(set3))
        for key, value in set_all.items():
            if value > 1:
                answer.append(key)
        return answer