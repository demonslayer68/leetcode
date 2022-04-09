class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            new_weight = stones[-1] - stones[-2]
            del (stones[-2])
            del (stones[-1])
            if not stones:
                return new_weight
            if new_weight:
                i = 0
                while i < len(stones) and new_weight > stones[i]:
                    i += 1
                stones.insert(i, new_weight)
        return stones[0]
