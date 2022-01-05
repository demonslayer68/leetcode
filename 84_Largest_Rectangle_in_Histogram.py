class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(-1)
        area = heights[0]
        rects = {heights[0]:0}
        for i in range(1, len(heights)):
            if heights[i] not in rects:
                rects[heights[i]] = i
            for height in list(rects.keys()):
                if heights[i] < height:
                    area = max(area, height * (i - rects[height]))
                    rects[heights[i]] = min(rects[height], rects[heights[i]])
                    del rects[height]
        return max(area,0)

obj = Solution()
print(obj.largestRectangleArea([8,7,9,8]))