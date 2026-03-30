class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        max_count = 0
        for i in nums:
            if i - 1 in sett:
                continue
            cur = i
            count = 1
            while cur + 1 in sett:
                count += 1
                cur += 1

            max_count = max(max_count, count)

        return max_count