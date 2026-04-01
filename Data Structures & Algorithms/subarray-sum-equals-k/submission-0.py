class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen_sum = defaultdict(int)
        last = 0
        count = 0
        seen_sum[0] = 1
        for i in range(len(nums)):
            last += nums[i]
            if last - k in seen_sum:
                count += seen_sum[last - k]
            seen_sum[last] += 1
        return count