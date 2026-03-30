class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def backtrack(current, opened, closed):
            if opened == closed == n:
                self.ans.append("".join(current))
                return

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

            