class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        count = 0
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            else:
                if res[-1][1] > intervals[i][0]:
                    count += 1
                    if intervals[i][1] < res[-1][1]:
                        res[-1] = intervals[i]

                else:
                    res.append(intervals[i])

        return count
            