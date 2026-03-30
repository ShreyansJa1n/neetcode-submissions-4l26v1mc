class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def backtrack(current, opened, closed):
            if opened > n or closed > n:
                return
            if opened == closed == n:
                self.ans.append("".join(current))

            if opened < n:
                current.append("(")
                backtrack(current, opened + 1, closed)
                current.pop()

            if closed < opened:
                current.append(")")
                backtrack(current, opened, closed + 1)
                current.pop()

            return

        backtrack([], 0, 0)
        return self.ans

            