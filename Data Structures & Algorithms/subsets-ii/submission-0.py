class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        self.ans = []
        def backtrack(start, current):
            self.ans.append(current[:])
            if start == len(nums):
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

            return

        backtrack(0, [])
        return self.ans
            