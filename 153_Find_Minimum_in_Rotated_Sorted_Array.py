class Solution:
    def findMin(self, nums: list[int]) -> int:
        # edge cases of one element and smallest = 0
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        minm, maxm = 0, len(nums) - 1
        while minm <= maxm:
            index = (minm + maxm) // 2
            # this is the min point
            if nums[index] < nums[index-1]:
                return nums[index]
            elif nums[index] < nums[0]:
                maxm = index - 1
            else:
                minm = index + 1
