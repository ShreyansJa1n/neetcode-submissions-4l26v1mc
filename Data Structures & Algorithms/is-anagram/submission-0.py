class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_c = {}
        t_c = {}
        for i in range(len(s)):
            if s[i] in s_c:
                s_c[s[i]] += 1
            else:
                s_c[s[i]] = 1

        for i in range(len(t)):
            if t[i] in t_c:
                t_c[t[i]] += 1
            else:
                t_c[t[i]] = 1

        return s_c == t_c