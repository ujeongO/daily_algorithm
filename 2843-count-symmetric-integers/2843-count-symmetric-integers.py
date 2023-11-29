class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0
        for num in range(low, high+1):
            num = str(num)
            if len(num)%2 != 0:
                continue
            num1 = num[:len(num)//2]
            num2 = num[len(num)//2:]
            sum1, sum2 = 0, 0

            for i in range(len(num)//2):
                sum1 += int(num1[i])
                sum2 += int(num2[i])
                
            if sum1 == sum2:
                answer += 1
        return answer