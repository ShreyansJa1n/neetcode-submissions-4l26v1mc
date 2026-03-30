class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def backtrack(start, current, summ, choices):
            if summ > target:
                return
            if summ == target:
                self.ans.append(current[:])
            
            for i in range(len(choices)):
                current.append(choices[i])
                backtrack(i + 1, current, summ + choices[i], choices[i:])
                current.pop()

        backtrack(0, [], 0, nums)
        return self.ans

