class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        first_index = nums.index(1)
        last_index = nums.index(len(nums))
        print(first_index, last_index)
        # 1은 맨 앞으로 가야함
        # 즉, 현재 인덱스 만큼 앞으로 이동하면 됨
        # n은 맨 뒤로 가야함
        # 즉, 배열 전체 길이에서 현재 인덱스만큼 빼주면 됨
        answer = (len(nums) - last_index) + first_index - 1
        # 이 때, 1이 n보다 뒤에 있으면, 연산을 한번 더 적게 하게 됨
        if first_index > last_index:
            answer -= 1

        return answer 