class Solution:
    def splitNum(self, num: int) -> int:
        num_str = sorted(str(num))
        num1, num2 = "", ""
        for i, c in enumerate(num_str):
            if i % 2 == 0:
                num1 += c
            else:
                num2 += c
        return int(num1) + int(num2)