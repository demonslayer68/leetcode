class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # storing cache of the format (k, start)
        # the cache represents the set of k size combinations with first number = start
        # initially I thought of using with first number >= start.
        # But that will be a lot of wasted storage, for minimal gain.
        # instead now running a loop for number >= start

        cache = {}
        def rec_combine(n, k, start):
            if k == 1:
                return [[start]]
            if (k, start) not in cache:
                combs = []
                for i in range(start + 1, n - k + 3):
                    combs += rec_combine(n, k - 1, i)
                cache[(k, start)] = [[start] + elem for elem in combs]
            return cache[(k, start)]

        output = []
        for i in range(1, n - k + 2):
            output += rec_combine(n, k, i)
        return output
