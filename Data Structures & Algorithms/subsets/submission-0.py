class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []

        def backtrack(start, current):
            self.ans.append(current[:])
            if start >= len(nums):
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()

        backtrack(0, [])
        return self.ans
            