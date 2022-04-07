class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if that last 2 digits are in ascending, then just switch
        if len(nums) == 0 or len(nums) == 1:
            return nums

        if nums[-1] > nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]

        else:
            i = len(nums) - 1
            while i > 0 and nums[i] <= nums[i - 1]:
                i -= 1
            temp = nums[i:]
            temp.reverse()
            nums[i:] = temp
            if i != 0:
                j = i
                while nums[i - 1] >= nums[j]:
                    j += 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
