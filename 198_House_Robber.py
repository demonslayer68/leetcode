class Solution:
    def rob(self, nums: list[int]) -> int:
        mem = {}

        def recursiveRob(start):
            # reached the end
            if start >= len(nums):
                return 0
            elif start not in mem:
                # you can always either rob +2 or +3 house to be optimal
                mem[start] = nums[start] + max(recursiveRob(start+2), recursiveRob(start+3))
                return mem[start]

        return max(recursiveRob(0), recursiveRob(1))

obj = Solution()
obj.rob([1,2,3,1])
