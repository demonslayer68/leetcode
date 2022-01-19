class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]):
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        remove = 0
        for i in range(1, len(intervals)):
            # whenever we encounter an overlap, we remove the interval with larger end
            if intervals[i][0] < end:
                remove += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
        return remove
