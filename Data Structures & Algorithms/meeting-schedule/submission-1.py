"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, lst: List[Interval]) -> bool:
        intervals = []
        for i in lst:
            intervals.append([i.start,i.end])
        n = len(intervals)
        intervals.sort(key=lambda x:x[1])
        for i in range(1,n):
            px,py = intervals[i - 1]
            cx,cy = intervals[i]
            if(cx < py):
                return False

        return True
