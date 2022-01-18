class Solution:
    def maxDistToClosest(self, seats):
        maxd = 0
        i = 0
        while not seats[i]:
            i += 1
        curr = i
        maxd = i
        for i in range(i + 1, len(seats)):
            if seats[i]:
                maxd = max(maxd, (i - curr) // 2)
                curr = i

        maxd = max(maxd, len(seats) - 1 - curr)
        return maxd
