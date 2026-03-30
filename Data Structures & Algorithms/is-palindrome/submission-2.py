class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < len(s) and not str.isalnum(s[left]):
                left += 1    
            while right >= 0 and not str.isalnum(s[right]):
                right -= 1
            if left < len(s) and right >= 0 and str.lower(s[left]) != str.lower(s[right]):
                return False
            left += 1
            right -= 1

        return True