class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        # iterate to find 0s
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in visited and matrix[i][j] == 0:
                    # update all non zeros in the same row and column to 0 and mark as visited
                    for x in range(len(matrix)):
                        if matrix[x][j] != 0:
                            matrix[x][j] = 0
                            visited.add((x, j))
                    for y in range(len(matrix[0])):
                        if matrix[i][y] != 0:
                            matrix[i][y] = 0
                            visited.add((i, y))