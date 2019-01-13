# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []

        if not intervals:
            return result

        length  = len(intervals)
        if length<2:
            return [intervals[0]]

        # naive solution O(N*log(N))
        intervals = sorted(intervals, key=lambda x: x.start)
        ind1, ind2 = 0, 1
        while ind2<length:
            if intervals[ind1].end<intervals[ind2].start:
                result.append(intervals[ind1])
                ind1=ind2
                ind2+=1
            else:
                if intervals[ind1].end < intervals[ind2].end:
                    intervals[ind1].end = intervals[ind2].end
                ind2+=1

        result.append(intervals[ind1])
        return result
               

