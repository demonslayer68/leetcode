class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        output = 0

        def findIsland(i, j):
            # keep expanding and mark all parts of the island as -1
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "-1"
                for x, y in [[i, j + 1], [i + 1, j], [i - 1, j], [i, j - 1]]:
                    findIsland(x, y)

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                # on finding land, find the full island
                if grid[m][n] == "1":
                    output += 1
                    findIsland(m, n)
        return output
