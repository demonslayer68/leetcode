class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        judges = set(range(1, n+1))
        count = [0] * ( n + 1)
        judge = -1
        for pair in trust:
            judges.discard(pair[0])
            count[pair[1]] += 1

        for x in judges:
            if count[x] == n - 1:
                if judge == -1:
                    judge = x
                else:
                    return -1
        return judge
