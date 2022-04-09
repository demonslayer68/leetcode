class KthLargest:
    sorted_nums = []
    k = 0

    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums, reverse=True)
        self.k = k

    def add(self, val: int) -> int:
        i = len(self.sorted_nums) - 1
        while i >= 0 and self.sorted_nums[i] < val:
            i -= 1

        # if this condition doesn't hold, then we just skip the number since it is smaller than k largest
        if i <= len(self.sorted_nums) - 1:
            self.sorted_nums.insert(i + 1, val)
            if len(self.sorted_nums) > self.k:
                del (self.sorted_nums[-1])
        return self.sorted_nums[self.k - 1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)