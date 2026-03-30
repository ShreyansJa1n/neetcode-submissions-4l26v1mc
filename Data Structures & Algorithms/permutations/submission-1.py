class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(visited, current):
            if len(current) == len(nums):
                self.ans.append(current[:])

            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                current.append(nums[i])
                backtrack(visited, current)
                current.pop()
                visited.remove(nums[i])

            return

        backtrack(set(), [])
        return self.ans

            