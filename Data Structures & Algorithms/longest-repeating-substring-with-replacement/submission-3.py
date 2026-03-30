class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        l, r = 0, 0
        max_window = 0
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            if r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            else:
                max_window = max(max_window, r - l + 1)
            r += 1

        return max_window
