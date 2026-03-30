class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False

        target = sum_nums // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            if dp[target] == True:
                return True
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True

        return dp[target]
