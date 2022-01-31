class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxm = 0
        for elem in accounts:
            maxm = max(maxm, sum(elem))
        return maxm
