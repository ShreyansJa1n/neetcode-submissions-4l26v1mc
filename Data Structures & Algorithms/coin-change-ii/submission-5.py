class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] = dp.get(i, 0) + dp.get(i - coin, 0)

        return dp[amount]