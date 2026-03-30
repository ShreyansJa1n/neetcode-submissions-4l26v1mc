class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [0] * len(nums)
        prefix_prod[0] = 1
        suffix_prod = [0] * len(nums)
        suffix_prod[-1] = 1

        for i in range(1, len(prefix_prod)):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]

        for i in range(len(suffix_prod) - 2, -1, -1):
            suffix_prod[i] = suffix_prod[i+1] * nums[i+1]

        res = []
        for i in range(len(nums)):
            res.append(prefix_prod[i] * suffix_prod[i])
        return res