class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumcount = {0: 1}
        sums = 0
        count = 0
        for i in range(len(nums)):
            sums += nums[i]
            count += sumcount.get(sums - k, 0)
            sumcount[sums] = sumcount.get(sums, 0) + 1
        return count
