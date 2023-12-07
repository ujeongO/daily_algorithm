class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # set.issubset
        collection = set()
        target = set([x+1 for x in range(k)])
        nums = reversed(nums)
        cnt = 0
        for i, num in enumerate(nums):
          cnt += 1
          if num > k:
            continue
          collection.add(num)
          print(collection)
          if target.issubset(collection):
            return cnt