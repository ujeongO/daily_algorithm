class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        answer = []
        for i in range(1, len(mountain)-1):
            print(mountain[i], mountain[i-1], mountain[i+1])
            # 앞에 위치한 수보다 크고, 뒤에 위치한 수보다 크다면
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                # answer에 i를 추가한다.
                answer.append(i)
        return answer