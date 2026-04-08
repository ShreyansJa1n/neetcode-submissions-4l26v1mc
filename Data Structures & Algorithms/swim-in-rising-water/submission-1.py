class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        min_heap = [[grid[0][0], 0, 0]]
        n = len(grid)
        visited = set()
        while min_heap:
            time, i, j = heapq.heappop(min_heap)
            if i == n - 1 and j == n - 1:
                return time
            
            for r, c in directions:
                nr, nc = i + r, j + c
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, [max(time, grid[nr][nc]), nr, nc])
            
        return 0