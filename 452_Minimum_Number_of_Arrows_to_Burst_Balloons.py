class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # sort by start point
        points.sort(key=lambda x: x[0])
        current_end = points[0][1]
        count = 1
        for i in range(1, len(points)):
            # if the next point is in range, add to range and modify end point
            # ( start point is already sorted, so taken care of )
            if points[i][0] <= current_end:
                current_end = min(current_end, points[i][1])
            # create a new range and count an extra arrow
            else:
                count += 1
                current_end = points[i][1]
        return count
