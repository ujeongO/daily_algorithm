class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        if k > 0:
            for i in range(len(code)):
                cur_sum = 0
                for j in range(k):
                    cur_sum += code[(i+j+1) % len(code)]
                answer.append(cur_sum)
        elif k < 0:
            for i in range(len(code)):
                cur_sum = 0
                for j in range(-k):
                    cur_sum += code[(i-j-1)]
                answer.append(cur_sum)
        elif k == 0:
            answer = [0]*len(code)
        return answer