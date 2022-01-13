import collections


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # faster than list
        q = collections.deque([])
        nearest = []
        # append all 0 elements to queue
        for i in range(len(mat)):
            nearest.append([])
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    nearest[i].append(0)
                else:
                    nearest[i].append(-1)

        # recursively expand to all nearby elements, increasing the distance by 1
        while q:
            x, y = q.popleft()
            for a, b in [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]:
                if a < 0 or b < 0 or a >= len(mat) or b >= len(mat[0]) or nearest[a][b] != -1:
                    continue
                nearest[a][b] = nearest[x][y] + 1
                q.append((a, b))

        return nearest
