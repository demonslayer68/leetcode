class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = nums[0:len(nums) - k:1]
        for i in range(len(nums) - k, len(nums)):
            nums[i - len(nums) + k] = nums[i]
        for i in range(0, len(nums) - k):
            nums[k + i] = temp[i]
        print(nums)


obj = Solution()
obj.rotate([1,2,3,4,5,6,7], 3)