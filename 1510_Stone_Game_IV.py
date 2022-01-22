import math


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        mem = {}

        def is_winner_rec(m):
            # base case
            if m == 1:
                return True
            # perfect sq root
            if m not in mem:
                s = math.sqrt(m)
                i = int(s)
                if i == s:
                    mem[m] = True
                    return mem[m]
                mem[m] = False
                # starting in reverse for faster runtime
                while i > 0:
                    if not is_winner_rec(m - i ** 2):
                        mem[m] = True
                        break
                    i -= 1
            return mem[m]
        return is_winner_rec(n)
