class Solution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        data = {}
        for i in range(0, len(nums)):
            if target - nums[i] in data:
                j = nums.index(target - nums[i])
                return [i, j]
            else:
                data[nums[i]] = i


obj = Solution()
x = obj.twosum([1, 2, 3, 6, 5],3)
print(x)
