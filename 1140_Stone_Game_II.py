class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        mem = {}

        def recursive_pick(start, m, total):
            # if the remaining piles are <2m, pick all
            if start + 2 * m >= len(piles):
                return total
            if (start, m) not in mem:
                minloss = total
                savedtotal = total
                # for each value of x <=2m, pick that piles and minimize opponent profit
                # we keep adjusting total to indicate the pile we have removed as x increases
                for i in range(start, start + 2 * m):
                    total = total - piles[i]
                    loss = recursive_pick(i+1, max(m, i - start + 1), total)
                    if loss < minloss:
                        minloss = loss
                mem[(start, m)] = savedtotal - minloss
            return mem[(start, m)]

        ftotal = sum(piles)
        return recursive_pick(0, 1, ftotal)
