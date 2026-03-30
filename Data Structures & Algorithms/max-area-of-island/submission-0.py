class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        self.max_area = 0
        def bfs(i, j):
            q = deque([[i, j]])
            visited.add((i, j))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            area = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    if (row + dr, col + dc) not in visited and row + dr >= 0 and row + dr < len(grid) and col + dc >= 0 and col + dc < len(grid[0]) and grid[row + dr][col + dc] == 1:
                        visited.add((row + dr, col + dc))
                        q.append([row + dr, col + dc])
                        area += 1

            self.max_area = max(self.max_area, area)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    bfs(i, j)
        return self.max_area
