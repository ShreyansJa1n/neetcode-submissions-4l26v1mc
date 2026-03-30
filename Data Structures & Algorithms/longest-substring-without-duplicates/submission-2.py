class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_count = 0
        hashset = set()
        while r < len(s):
            if s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            else:
                hashset.add(s[r])
                r += 1
                max_count = max(max_count, (r - l) + 1)

        return max_count - 1 if max_count - 1 >=0 else 0
