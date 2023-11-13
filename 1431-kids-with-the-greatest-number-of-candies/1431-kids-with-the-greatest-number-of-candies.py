class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        # 1. 현재 candies에서 가장 큰 값 찾기
        maxCandy = max(candies)
        # 2. for문을 돌면서 현재 candy 개수와 extraCandies 합쳐주기
        for candy in candies:
            added_candy = candy + extraCandies
            # 3. 합친 값이 가장 큰 값보다 크면 True, 아니면 False를 answer에 추가해주기
            if added_candy >= maxCandy:
                answer.append(True)
            else:
                answer.append(False)
        return answer