class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        visited = set()
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                  visited.add((i, j))
                  q.append([i, j])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        steps = 1
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) not in visited and 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != -1:
                        grid[nr][nc] = steps
                        visited.add((nr, nc))
                        q.append([nr, nc])
            steps += 1


        return