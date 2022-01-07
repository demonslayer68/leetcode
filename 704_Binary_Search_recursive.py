class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def bs(nums, start, end, target):
            i = int((start + end ) / 2)
            if end <= start:
                if nums[i] == target:
                    return i
                else:
                    return -1
            elif nums[i] < target:
                return bs(nums, i + 1, end, target)
            elif nums[i] > target:
                return bs(nums, start, i - 1, target)
            else:
                return i

        return bs(nums,0,len(nums)-1,target)


obj = Solution()
print(obj.search([-1,0,3,5,9,12],9))