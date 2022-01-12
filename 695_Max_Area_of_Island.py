class Solution:
    size = 0

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        output = 0

        # expand till you reach all corners of island. then size holds island size
        def find_recursive(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                self.size += 1
                for pair in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                    find_recursive(pair[0], pair[1])

        # go to each cell, if its a new island, call recursive func
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    self.size = 0
                    find_recursive(x, y)
                    output = max(output, self.size)
        return output
