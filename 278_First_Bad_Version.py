# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while end >= start:
            i = int((start + end) / 2)
            if not isBadVersion(i):
                start = i + 1
            else:
                if isBadVersion(i-1):
                    end = i - 1
                else:
                    return i
        return -1
