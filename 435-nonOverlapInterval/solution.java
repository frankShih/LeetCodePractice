/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public int eraseOverlapIntervals(Interval[] intervals) {
        Arrays.sort(intervals, (a, b) -> 
                    (a.end == b.end ? /*b.start - a.start*/1 : a.end - b.end));
        // sorted by end (ascend)
        int end = Integer.MIN_VALUE, count = 0;
        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i].start >= end) end = intervals[i].end;
            else count++;
        }
        return count;
    }
}