class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = (0, 0)
        for i, row in enumerate(mat):
            one_cnt = row.count(1)
            # answer[1] 보다 one_cnt가 크다면
            # answer에 (i, one_cnt)를 할당
            if answer[1] < one_cnt:
                answer = (i, one_cnt)
        return answer