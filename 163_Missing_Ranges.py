class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        output = []
        # append lower - 1 and higher + 1, so that we can just solve uniformly
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 2:
                output.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                output.append(str(nums[i]+1) + "->" + str(nums[i+1] - 1))
        return output