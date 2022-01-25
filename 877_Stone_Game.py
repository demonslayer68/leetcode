class Solution:
    def stoneGame(self, piles):
        mem = {}

        def recursive_pick(start, end, total):
            # if only one pile is left, return that
            if start == end:
                return piles[start]
            # since each player plays optimally, we pick the side where the optimal score for the next pick is smallest
            # then do this recursively
            if (start, end) not in mem:
                mem[(start, end)] = total - min(recursive_pick(start + 1, end, total - piles[start]),
                                                recursive_pick(start, end - 1, total - piles[end]))
            return mem[(start, end)]

        ftotal = sum(piles)
        return recursive_pick(0, len(piles) - 1, ftotal) > ftotal // 2
