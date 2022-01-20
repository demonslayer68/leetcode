class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # calculate hours taken for a given k
        def calculatehours(k):
            hours = [-(-x // k) for x in piles]
            return sum(hours)

        # do binary search for k
        count = sum(piles)
        mink = max(count // h, 1)
        maxk = max(2 * mink, mink + len(piles))
        while mink <= maxk:
            estk = (mink + maxk) // 2
            if calculatehours(estk) <= h:
                if estk == 1 or calculatehours(estk - 1) > h:
                    break
                else:
                    maxk = estk - 1
            else:
                mink = estk + 1
        return estk
