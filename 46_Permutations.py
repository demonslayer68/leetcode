class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cache = {}

        # this function creates all permutations for nums[start:]. then recursively call from start = 0
        def rec_permute(start):
            startnum = nums[start]
            if start == len(nums) - 1:
                return [[startnum]]
            output = []
            perms = rec_permute(start + 1)
            for perm in perms:
                for i in range(len(perm) + 1):
                    output.append(perm[:i] + [startnum] + perm[i:])
            return output

        return rec_permute(0)
