class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        l, r = 0, len(nums)-1
        if target in nums:
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    answer = mid
                    break
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
        return answer