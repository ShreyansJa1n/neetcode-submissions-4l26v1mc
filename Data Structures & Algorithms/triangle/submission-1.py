class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            dp = [0] * len(triangle[i])
            for j in range(len(triangle[i])):
                dp[j] = min(triangle[i][j] + row[j], triangle[i][j] + row[j + 1])
            row = dp
        return row[0]