class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        res[0] = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            res[i] = max(res[i-1] + nums[i], nums[i])
            max_sum = max(max_sum, res[i])
        return max_sum