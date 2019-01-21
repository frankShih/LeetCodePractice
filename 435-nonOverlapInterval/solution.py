# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        length = len(intervals)

        '''

        # naively check endValue O(N*log(N)) 90%
        intervals=sorted(intervals ,key=lambda l:l.end, reverse=False)
        counter=0   # the number of non-overlapping intervals
        previous_end=float('-inf')

        for i in range(0, length):
            if previous_end<=intervals[i].start:
                previous_end=intervals[i].end
                counter+=1
                # print(pre.start, pre.end)

        return length - counter

        '''

        # naively check startValue O(N*log(N)) 52%
        intervals=sorted(intervals ,key=lambda l:l.start, reverse=True)
        counter=0
        previous_start=float('inf')

        for interval in intervals:
            if previous_start>=interval.end:
                # over-lapping occured
                previous_start=interval.start
            else:
                counter+=1

        return counter
