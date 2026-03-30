class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(visited):
            if len(visited) == len(nums):
                self.ans.append(visited[:])

            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                visited.append(nums[i])
                backtrack(visited)
                visited.pop()

            return

        backtrack([])
        return self.ans

            