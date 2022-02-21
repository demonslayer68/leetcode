class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 1
        count = 0
        while i < len(nums) and j < len(nums):
            if i == j:
                j += 1
                continue
            if nums[i] > nums[j] - k:
                j += 1
            elif nums[i] < nums[j] - k:
                i += 1
            else:
                count += 1
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
        return count
