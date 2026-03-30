class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        res = []
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])

            else:
                if res[-1][1] < intervals[i][0]:
                    res.append(intervals[i])
                else:
                    res[-1][1] = max(res[-1][1], intervals[i][1])
        
        return res