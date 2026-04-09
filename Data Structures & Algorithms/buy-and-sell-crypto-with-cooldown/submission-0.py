class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                hold = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, hold)

            else:
                sell = dfs(i + 2, not buying) + prices[i]
                hold = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, hold)

            return dp[(i, buying)]

        return dfs(0, True)