class Solution:
    def search(self, nums: list[int], target: int) -> int:
            start = 0
            end = len(nums) - 1
            while end >= start:
                i = int((start + end) / 2)
                if nums[i] < target:
                    start = i + 1
                elif nums[i] > target:
                    end = i - 1
                else:
                    return i
            return -1


obj = Solution()
print(obj.search([-1,0,3,5,9,12],9))