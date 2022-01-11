from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        elems = Counter(nums)
        prev = 0
        prev_prev = 0
        current = 0
        prev_key = min(elems.keys()) - 2
        for key in sorted(elems):
            # if keys are not next to each other, you can always pick current element
            if key - prev_key != 1:
                current = key * elems[key] + max(prev, prev_prev)
            # else, you need to add current element to only prev_prev, since prev will delete current element
            else:
                current = max(key * elems[key] + prev_prev, prev)
            prev_prev = prev
            prev = current
            prev_key = key
        return current

