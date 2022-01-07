from decimal import *

class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        mem = {}

        # count is number of elements we need to use such that sum(elements) = target
        # index is the start index
        # there could probably be a way to optimize this instead of running over all Ks, but can't think of it
        def findsubset(target, count, index):
            if count == 0:
                return target == 0

            # not adding = here, since if the last element satisfies the condition, then we will exceed length by 1
            # but that is fine since the next recursion will hit only the above statement
            if count + index > len(nums):
                return False

            if (count, index, target) not in mem:
                mem[(count, index, target)] = findsubset(target - nums[index], count - 1, index + 1) or \
                                              findsubset(target, count, index + 1)
            return mem[(count, index, target)]

        average = Decimal(sum(nums)) / Decimal(len(nums))
        for i in range(1, len(nums) // 2 + 1):
            if int(i * average) == i * average:
                if findsubset(i * average, i, 0):
                    return True
        return False


obj = Solution()
print(obj.splitArraySameAverage([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]))
