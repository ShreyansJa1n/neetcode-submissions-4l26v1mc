class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        l = 0
        result = []
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            while q and q[0] < l:
                q.popleft()
            q.append(r)
            if r - l + 1 == k:
                result.append(nums[q[0]])
                l += 1
        return result