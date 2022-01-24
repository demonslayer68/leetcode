class Solution:
    def search(self, nums: list[int], target: int) -> int:
        minm = 0
        maxm = len(nums) - 1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if nums[0] < nums[-1]:
            start = 0
        else:
            while minm <= maxm:
                start = (minm + maxm) // 2
                if start == 0:
                    start = 1
                if nums[start] < nums[start - 1]:
                    break
                elif nums[start] > nums[0]:
                    minm = start + 1
                else:
                    maxm = start - 1

        # binary search
        minm = 0
        maxm = len(nums) - 1
        while minm <= maxm:
            index = (minm + maxm) // 2
            findex = (start + index) % len(nums)
            if nums[findex] == target:
                return findex
            elif nums[findex] < target:
                minm = index + 1
            else:
                maxm = index - 1
        return -1
