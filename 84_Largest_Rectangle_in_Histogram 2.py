class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(-1)
        area = heights[0]
        rects = [[-1,-1],[0,0]]
        for i in range(1, len(heights)):
            left = i
            while heights[i] < heights[rects[-1][0]]:
                start = rects.pop()
                area = max(area, heights[start[0]] * (i - start[1]))
                left = min(left, start[1])
            rects.append([i,left])
        return max(area,0)

obj = Solution()
print(obj.largestRectangleArea([3,2,4]))