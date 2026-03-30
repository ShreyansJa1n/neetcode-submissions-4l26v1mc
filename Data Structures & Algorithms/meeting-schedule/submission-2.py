"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x:x.start)
        last = intervals[0].end if intervals else 0
        for i in range(1, len(intervals)):
            if intervals[i].start < last:
                return False
            else:
                last = intervals[i].end

        return True