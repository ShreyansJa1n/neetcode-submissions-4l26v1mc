class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    oranges += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        oranges -= 1
                        q.append((nr, nc))
            if q:
                time += 1

        return time if oranges == 0 else -1
