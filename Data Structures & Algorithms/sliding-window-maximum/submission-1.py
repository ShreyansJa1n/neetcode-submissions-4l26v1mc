class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()  # stores indices
        l = 0
        result = []

        for r in range(len(nums)):
            # Step 1: clean right

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Step 2: clean left
            while q and q[0] < l:
                q.popleft()

            # Step 3: append r
            q.append(r)

            # Step 4: record result once window hits size k
            if r - l + 1 == k:
                result.append(nums[q[0]])
                l += 1

        return result
