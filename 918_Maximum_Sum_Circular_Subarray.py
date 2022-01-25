class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # get max subarry within given array
        def maxSubArray(arr):
            max_contin = arr[0]
            output = arr[0]
            for i in range(1, len(arr)):
                max_contin = max(max_contin + arr[i], arr[i])
                output = max(output, max_contin)
            return output

        revnums = [-1 * x for x in nums]
        # you do negative of array and call max array, then the leftover elements is the circular max
        # (since picked elements are actually the min)
        # the if else is for handling the edge case of all negative
        return max(nums) if max(nums) < 0 else max(maxSubArray(nums), -1 * (sum(revnums) - maxSubArray(revnums)))