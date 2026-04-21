class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        self.max_val = 0

        def dfs(i, j, prevVal):
            if i < 0 or i == m or j < 0 or j == n or matrix[i][j] <= prevVal:
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            
            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))

            dp[i][j] = res
            self.max_val = max(self.max_val, res)

            return res

        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)

        return self.max_val
        


            