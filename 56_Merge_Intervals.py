class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        output = []
        #sort
        intervals.sort(key = lambda x: x[0])
        output.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output

obj = Solution()
print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))
