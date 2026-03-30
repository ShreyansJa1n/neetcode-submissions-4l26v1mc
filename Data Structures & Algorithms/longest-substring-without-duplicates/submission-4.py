class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_count = 0
        last_seen = {}
        while r < len(s):
            if s[r] in last_seen:
                l = max(l, last_seen[s[r]] + 1)
            max_count = max(max_count, (r - l) + 1)
            last_seen[s[r]] = r
            r += 1
        return max_count