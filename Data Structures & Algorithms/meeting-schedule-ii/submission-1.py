"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x:x.start)
        max_rooms = 0
        heap = []
        for i in range(len(intervals)):
            if len(heap) == 0:
                heapq.heappush(heap, intervals[i].end)

            else:
                if intervals[i].start >= heap[0]:
                    heapq.heappop(heap)
                
                heapq.heappush(heap, intervals[i].end)

            max_rooms = max(max_rooms, len(heap))


        return max_rooms