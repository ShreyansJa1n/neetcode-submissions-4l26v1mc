class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def bfs(i, j):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            q = deque([[i, j]])
            visited.add((i, j))
            while q:
                row, col = q.popleft()
                for r,c in directions:
                    if row + r >= 0 and row + r < len(grid) and col + c >= 0 and col + c < len(grid[0]) and grid[row + r][col + c] == "1" and (row + r, col + c) not in visited:
                        visited.add((row + r, col + c))
                        q.append([row + r, col + c])
                        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    bfs(i, j)
        return islands
