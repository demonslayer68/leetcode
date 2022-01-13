import collections


class Solution:
    def orangesRotting(self, mat: list[list[int]]) -> int:
        # faster than list
        q = collections.deque([])
        count = 0
        minutes = -1
        timeend = ()
        # append all 2 elements to queue
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 2:
                    q.append((i, j))
                    timeend = (i, j)
                elif mat[i][j] == 1:
                    count += 1

        # recursively mark oranges as rotten.
        # update count for each rotten orange
        # track each minute by tracking last element
        while q:
            x, y = q.popleft()
            for a, b in [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]:
                if a < 0 or b < 0 or a >= len(mat) or b >= len(mat[0]) or mat[a][b] != 1:
                    continue
                count -= 1
                mat[a][b] = 2
                q.append((a, b))
            if (x, y) == timeend:
                minutes += 1
                timeend = (0, 0) if not q else q[-1]

        return -1 if count else max(minutes, 0)
