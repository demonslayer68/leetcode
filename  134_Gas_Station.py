class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        netcost = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(netcost) < 0:
            return -1
        start = 0
        while netcost[start] < 0:
            start += 1
        total = netcost[start]
        for i in range(start + 1, len(netcost)):
            total += netcost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start
