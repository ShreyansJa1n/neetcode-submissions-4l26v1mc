class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        best_l = 0
        best_r = 0

        for i in range(len(s)):
            left = i
            right = i

            while left >=0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    best_l = left
                    best_r = right
                left -= 1
                right += 1

            left = i
            right = i + 1

            while left >=0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    longest = right - left + 1
                    best_l = left
                    best_r = right
                left -= 1
                right += 1
                

        return s[best_l : best_r + 1]