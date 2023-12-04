class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        # 양 사이드 제외
        # 주위보다 큰 수의 인덱스 반환
        answer = []
        for i in range(1, len(mountain)-1):
            if (mountain[i-1] < mountain[i]) and (mountain[i] > mountain[i+1]):
                answer.append(i)
        return answer