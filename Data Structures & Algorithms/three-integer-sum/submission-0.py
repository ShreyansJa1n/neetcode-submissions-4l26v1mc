class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for idx, i in enumerate(sorted_nums):
            target = 0 - i

            left = idx + 1
            right = len(sorted_nums) - 1
            while left < right:
                summ = sorted_nums[left] + sorted_nums[right]

                if summ > target:
                    right -= 1
                elif summ < target:
                    left += 1
                else:
                    triplet = [sorted_nums[idx], sorted_nums[left], sorted_nums[right]]
                    if triplet not in res:
                        res.append(triplet)
                    left += 1
                    right -= 1

        return res