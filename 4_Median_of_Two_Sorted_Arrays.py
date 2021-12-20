class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i = 0
        j = 0
        curr = 0
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1 + len2
        saved = 0
        while 1:
            if j == len2 or ( i < len1 and nums1[i] < nums2[j] ):
                curr = nums1[i]
                i = i + 1
            else:
                curr = nums2[j]
                j = j + 1
            if i + j >= total / 2:
                if total % 2 == 1:
                    return curr
                elif i + j == total / 2:
                    saved = curr
                else:
                    return (curr + saved ) / 2

obj = Solution()
print( obj.findMedianSortedArrays([0,0],[0,0]) )

