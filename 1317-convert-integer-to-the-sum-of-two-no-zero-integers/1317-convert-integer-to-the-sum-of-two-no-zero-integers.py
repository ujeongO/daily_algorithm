class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            diff = n - i
            i_str = str(i)
            diff_str = str(diff)
            if "0" not in i_str and "0" not in diff_str:
                answer = [i, diff]
                break
        return answer