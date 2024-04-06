class Solution:
    def minPartitions(self, n: str) -> int:
        # 1. if) 입력이 한 자리 숫자 -> 숫자의 값만큼의 숫자를 더해야 함.
        # 2. if) 입력에 여러 자릿수 -> 각 자릿수를 독립적으로 풀고 
        # 2-1. 답 병합 -> 해당 입력에 합산되는 숫자를 만들 수 있음.
        # 3. => 최대 숫자와 같음.
        n_list = list(map(int, str(n)))
        return max(n_list)