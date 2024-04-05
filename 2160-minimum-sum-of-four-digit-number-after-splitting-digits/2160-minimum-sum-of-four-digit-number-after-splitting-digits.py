class Solution:
    def minimumSum(self, num: int) -> int:
        # 1. num -> 리스트화
        # 2. 오름차순 정렬 -> 작은 수가 십의자리
        # 3. 나머지는 일의자리 => 두 변수 합 리턴
        new1, new2 = '', ''
        s_num = sorted(list(str(num)))
        for i in range(len(s_num)):
            if i % 2:
                new2 += s_num[i]
            else:
                new1 += s_num[i]

        return int(new1) + int(new2)