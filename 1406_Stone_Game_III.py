class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        mem = {}

        def recursive_pick(start, total):
            # if we have reached the end, opponent will pick 0
            if start == len(stoneValue):
                return 0
            # if we are in last block, opponent will pick last. This block is explained below
            if start == len(stoneValue) - 1:
                return total
            if start not in mem:
                minloss = float("inf")
                savedtotal = total
                # For each number of stones, pick that many piles and minimize opponent profit
                # We keep adjusting total to indicate the pile we have removed as i increases
                # Now, because numbers can be negative, we don't by default pick up all in the end
                # This is handled by using the 2 base cases above, because in some cases total < 0, so better
                # to not pickup the stones in the end
                for i in range(start, min(start + 3, len(stoneValue))):
                    total = total - stoneValue[i]
                    loss = recursive_pick(i + 1, total)
                    if loss < minloss:
                        minloss = loss
                mem[start] = savedtotal - minloss
            return mem[start]

        ftotal = sum(stoneValue)
        output = recursive_pick(0, ftotal)
        if output > ftotal / 2:
            return "Alice"
        elif output < ftotal / 2:
            return "Bob"
        else:
            return "Tie"
