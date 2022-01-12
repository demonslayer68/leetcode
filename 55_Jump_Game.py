class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # doing iterative, since it is much faster than recursive( number of calls is extremely high )
        pos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= pos:
                pos = i
        return pos == 0
