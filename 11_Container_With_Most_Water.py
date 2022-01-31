class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        area = 0
        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            # we can directly exclude i, if h[i] < h[j], because all combinations with h[i] will not give max area
            # for some other k < j, if h[i] <= h[k] then area = h[i] * (k-i) < h[i] *(j-i)
            # if h[k] < h[i], then h[k] *(k - i) < h[i] *(k-i) which is even smaller
            # so safe to fully exclude i if h[i] < h[j] and vice versa
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area
