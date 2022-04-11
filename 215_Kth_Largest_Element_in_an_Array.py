class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = nums[0:k]
        largest.sort(reverse=True)
        for i in range(k, len(nums)):
            j = k - 1
            while j >= 0 and nums[i] >= largest[j]:
                j -= 1
            if j < k - 1:
                largest.insert(j + 1, nums[i])
                del (largest[-1])
        return largest[-1]
