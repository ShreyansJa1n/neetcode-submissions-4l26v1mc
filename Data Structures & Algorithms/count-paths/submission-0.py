class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

        return ways[m - 1][n - 1]