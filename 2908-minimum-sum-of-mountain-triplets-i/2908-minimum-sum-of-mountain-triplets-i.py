class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        answer = -1
        candidates = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    # 가운데 위치한 인덱스의 수가 제일 큰지 비교
                    # mountain이라면 합을 구해서, answer보다 작다면 지정
                    # 이 때 -1일 경우 고려
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        cur_sum = nums[i]+nums[j]+nums[k]
                        candidates.append(cur_sum)
        if not candidates:
            return -1
        return min(candidates)