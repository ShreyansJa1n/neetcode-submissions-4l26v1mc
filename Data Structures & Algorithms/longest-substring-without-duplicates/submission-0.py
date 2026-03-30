class Solution:
    def check_dupe(self, s: str):
        if len(set(s)) == len(s):
            return False
        return True
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_count = 0
        while r < len(s):
            if self.check_dupe(s[l:r+1]):
                l += 1
            else:
                max_count = max(max_count, (r - l) + 1)
                r += 1

        return max_count
