class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices[:]
            for i in flights:
                s, d, cost = i
                temp[d] = min(cost + prices[s], temp[d])
            prices = temp[:]

        return prices[dst] if prices[dst] != float('inf') else -1