class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # left right at 0th index left -> buy, right -> sell
        # i will keep on moving the right pointer
        # on each ith iteration, if prices[right] < prices[left], left = right
        # else I calculate the profit and check it with the current max profit
        # i return the max profit
        
        left, right = 0, 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

        return max_profit