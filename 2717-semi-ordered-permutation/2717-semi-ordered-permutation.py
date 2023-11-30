class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        first_index = nums.index(1)
        last_index = nums.index(len(nums))
        print(first_index, last_index)
        if first_index < last_index:
            return first_index + (len(nums) -1 -last_index)
        else:
            return first_index + (len(nums) -1 -last_index) -1

        return 0
