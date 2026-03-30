class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        dp = [(1,1)] * len(nums)
        dp[0] = (nums[0],nums[0])
        for i in range(1, len(nums)):
            maxi = max(nums[i] * dp[i - 1][0], dp[i - 1][1] * nums[i] , nums[i])
            print(maxi)
            current_max = max(current_max, maxi)
            dp[i] = (maxi, min(nums[i] * dp[i - 1][1], nums[i], nums[i] * dp[i - 1][0]))

        print(dp)
        return current_max