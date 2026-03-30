class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_char = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if digits == "":
            return []
        self.res = []
        def dfs(current, index):
            if index == len(digits):
                self.res.append(''.join(current))
                return

            for i in range(len(digit_char[digits[index]])):
                current.append(digit_char[digits[index]][i])
                dfs(current, index + 1)
                current.pop()

        dfs([], 0)
        return self.res
        