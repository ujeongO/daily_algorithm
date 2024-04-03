class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # x -= 1 and num += 1
        # -> (num += 1) 2*t번 반복
        # => 최대의 x를 구할 것
        for i in range(2*t):
            num += 1
        return num