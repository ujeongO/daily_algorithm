class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # set
        # set.issubset
        collection = set()
        target = set([x+1 for x in range(k)])

        # operation 구현
        for i in range(len(nums)):
          collection.add(nums[len(nums) -1 -i])
          if target.issubset(collection):
              return i+1