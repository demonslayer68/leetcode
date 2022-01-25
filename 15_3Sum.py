class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []
        for i in range(0, len(nums) - 2):
            # boundary condition to stop
            if nums[i] + nums[i + 1] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # we use a single loop to save time and do it in n^2,
            # since we need to only move one variable to find te next triplet
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    # this is to handle duplicates
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    j += 1
        return output
