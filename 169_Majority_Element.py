from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = Counter(nums)
        for key, value in count.items():
            if value > len(nums) // 2:
                return key
