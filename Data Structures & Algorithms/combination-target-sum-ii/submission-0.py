class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        self.ans = []
        def backtrack(start, summ, current):
            if summ > target:
                return
            if summ == target:
                self.ans.append(current[:])

            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, summ + nums[i], current)
                current.pop()

            return

        backtrack(0, 0, [])
        return self.ans