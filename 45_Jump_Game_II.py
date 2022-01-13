class Solution:
    def jump(self, nums: list[int]) -> int:
        mem = {}
        steps = 1
        i = 0
        if len(nums) == 1:
            return 0
        while i + nums[i] < len(nums) - 1:
            fast = 0
            for k in range(i+1, min(i+nums[i]+1, len(nums))):
                if k + nums[k] > fast:
                    fast = k + nums[k]
                    i = k
            steps += 1
        return steps

obj = Solution()
print( obj.jump([1, 2, 3]))