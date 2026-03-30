class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        last_seen = (nums[0],nums[0])
        for i in range(1, len(nums)):
            maxi = max(nums[i] * last_seen[0], last_seen[1] * nums[i] , nums[i])
            current_max = max(current_max, maxi)
            last_seen = (maxi, min(nums[i] * last_seen[1], nums[i], nums[i] * last_seen[0]))
        return current_max