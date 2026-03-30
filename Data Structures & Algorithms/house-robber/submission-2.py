class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        house_2 = nums[0]
        house_1 = max(nums[0], nums[1])
        for i in range(2, n):
            temp = house_1
            house_1 = max(house_2 + nums[i], house_1)
            house_2 = temp

        return house_1