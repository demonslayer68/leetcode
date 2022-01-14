class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        output = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                output.append(intervals[i])
            elif intervals[i][0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else:
                output.append(newInterval)
                break
            i += 1
        if i == len(intervals):
            output.append(newInterval)
        output += intervals[i:]
        return output
