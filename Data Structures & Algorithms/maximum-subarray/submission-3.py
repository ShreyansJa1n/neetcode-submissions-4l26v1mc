class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            prev = max(prev + nums[i], nums[i])
            max_sum = max(max_sum, prev)
        return max_sum