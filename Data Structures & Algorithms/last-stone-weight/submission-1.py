class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            if abs(stone1-stone2) > 0:
                heapq.heappush(stones, -abs(stone1-stone2))

        return -stones[0] if stones else 0