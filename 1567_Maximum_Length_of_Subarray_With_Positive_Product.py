class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxlen = 0
        # tracker for max positive and negative list of numbers ( with ith number included )
        # then we iterate over i and dp
        pos = 0
        neg = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            elif nums[i] < 0:
                pos, neg = neg + 1 if neg > 0 else 0, pos + 1
            else:
                neg = 0
                pos = 0
            maxlen = max(maxlen, pos)
        return maxlen