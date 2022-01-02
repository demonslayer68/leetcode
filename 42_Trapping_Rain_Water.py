class Solution:
    def trap(self, height: list[int]) -> int:
        leftheight = [height[0]] * len(height)
        rightheight = [height[len(height)-1]] * len(height)
        water = 0

        for x in range(len(height)-2, -1, -1):
            if rightheight[x+1] < height[x]:
                rightheight[x] = height[x]
            else:
                rightheight[x] = rightheight[x+1]

        for x in range(1,len(height)):
            if leftheight[x-1] < height[x]:
                leftheight[x] = height[x]
            else:
                leftheight[x] = leftheight[x-1]
            water = water + min(leftheight[x], rightheight[x]) - height[x]

        return water

obj = Solution()
print(obj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))