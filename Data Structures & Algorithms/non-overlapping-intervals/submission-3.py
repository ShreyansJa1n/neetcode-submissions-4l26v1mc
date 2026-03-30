class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if res > intervals[i][0]:
                count += 1
                if intervals[i][1] < res:
                    res = intervals[i][1]
            else:
                res = intervals[i][1]

        return count
            