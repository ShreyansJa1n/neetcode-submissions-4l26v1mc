class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        matches = 0
        seen = {}
        lo, ro = 0, 0
        min_length = float('inf')

        t_counter = {}
        for i in t:
            t_counter[i] = t_counter.get(i, 0) + 1
        while r < len(s):
            if s[r] in t_counter:
                seen[s[r]] = seen.get(s[r], 0) + 1
                if seen[s[r]] == t_counter.get(s[r]):
                    matches += 1
            
            while matches == len(t_counter):
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    lo, ro = l, r
                if s[l] in t_counter:
                    seen[s[l]] -= 1
                    if seen[s[l]] < t_counter.get(s[l]):
                        matches -= 1
                l += 1
            r+=1

        return s[lo: ro+1] if min_length != float('inf') else ""
            
