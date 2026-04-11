class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(len(nums)):
            new_dp = defaultdict(int)
            for j in dp:
                new_dp[j - nums[i]] += dp[j]
                new_dp[j + nums[i]] += dp[j]
            dp = new_dp
        return dp[target]