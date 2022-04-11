class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                new_col = ( col + k ) % len(grid[0])
                new_row = (row + (col + k) // len(grid[0])) % len(grid)
                new_grid[new_row][new_col] = grid[row][col]
        return new_grid
