class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x,y in enumerate(nums):
            for i in range(x+1,len(nums)):
                if y + nums[i] == target:
                    return [x, i]

obj = Solution()
x = obj.twoSum([1,2,3,5],6)
print(x)
