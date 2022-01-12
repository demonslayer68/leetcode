class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        mem = {}

        def pick_recursive(i1, j1, i2, j2):
            if i1 == len(grid) - 1 and j1 == len(grid) - 1 and i2 == len(grid) - 1 and j2 == len(grid) - 1:
                return grid[-1][-1]
            if i1 == len(grid) or \
                    j1 == len(grid[0]) or \
                    i2 == len(grid[0]) or \
                    j2 == len(grid[0]) or \
                    grid[i1][j1] == -1 or \
                    grid[i2][j2] == -1:
                return -3000
            if (i1, j1, i2, j2) not in mem:
                if i1 == i2 and j1 == j2:
                    points = grid[i1][j1]
                else:
                    points = grid[i1][j1] + grid[i2][j2]
                mem[(i1, j1, i2, j2)] = points + max(pick_recursive(i1 + 1, j1, i2+1, j2),
                                                    pick_recursive(i1+1, j1, i2, j2+1),
                                                    pick_recursive(i1, j1+1, i2 + 1, j2),
                                                    pick_recursive(i1, j1+1, i2, j2 + 1))
            return mem[(i1, j1, i2, j2)]

        if grid[0][0] == -1 or grid[-1][-1] == -1:
            return 0
        else:
            return max(0, pick_recursive(0, 0, 0, 0))
