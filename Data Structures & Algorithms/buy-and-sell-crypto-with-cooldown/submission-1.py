class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = float('-inf')
        rest = 0

        for p in prices[1:]:
            hold, sold, rest = (
                max(hold, rest - p),
                hold + p,
                max(rest, sold)
            )

        return max(rest, sold)