class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mem = {} #dp storage

        # function to find the max cherries for a given row, position of robots
        def descend(row, pos1, pos2):
            if pos1 < 0 or pos1 >= cols or pos2 < 0 or pos2 >= cols:
                return 0
            if row == rows:
                return 0
            if (row, pos1, pos2) not in mem:
                future = 0
                for i in [pos1 - 1, pos1, pos1 + 1]:
                    for j in [pos2 - 1, pos2, pos2 + 1]:
                        future = max(future, descend(row + 1, i, j))
                if pos1 != pos2:
                    mem[(row, pos1, pos2)] = future + grid[row][pos1] + grid[row][pos2]
                else:
                    mem[(row, pos1, pos2)] = future + grid[row][pos1]
            return mem[(row, pos1, pos2)]

        return descend(0,0, cols - 1)
