class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(current, i, j):
            if i >= len(board) or j >= len(board[0]) or len(current) > len(word) or i < 0 or j < 0 or board[i][j] == "#":
                return False
            
            if current + board[i][j] == word:
                return True

            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            current += board[i][j]
            for r, c in directions:
                ch = board[i][j]
                board[i][j] = "#"
                res = backtrack(current, i+r, j+c)
                if res:
                    return True
                board[i][j] = ch

            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = backtrack("", i, j)
                    if res:
                        return True

        return False
                