class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_intervals = [x[0] for x in intervals]
        end_intervals = [x[1] for x in intervals]
        start_intervals.sort()
        end_intervals.sort()
        output = rooms = i = j = 0
        while i < len(intervals):
            rooms += 1
            while end_intervals[j] <= start_intervals[i]:
                rooms -= 1
                j += 1
            output = max(output, rooms)
            i += 1
        return output
