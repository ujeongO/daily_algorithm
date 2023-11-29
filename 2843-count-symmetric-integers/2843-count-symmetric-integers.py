class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0
        for i in range(low, high+1):
            num_str = str(i)
            # 길이가 홀수일 때 continue
            if len(num_str)%2 == 1:
                continue

            head = num_str[:len(num_str)//2]
            tail = num_str[len(num_str)//2:]
            if sum([int(c) for c in head]) == sum([int(c) for c in tail]):
                answer += 1
        return answer