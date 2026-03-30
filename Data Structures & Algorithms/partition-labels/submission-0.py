class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = 0
        size = 0
        last_seen = {}
        res = []
        for i in range(len(s)):
            last_seen[s[i]] = i
        
        for i in range(len(s)):
            if last_seen[s[i]] > end:
                end = last_seen[s[i]]
            size += 1
            if i == end:
                res.append(size)
                size = 0

        return res