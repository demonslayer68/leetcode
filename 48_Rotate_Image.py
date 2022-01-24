class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                pairs = [[i, j], [n - 1 - j, i], [n - 1 - i, n - 1 - j], [j, n - 1 - i]]
                temp = matrix[i][j]
                for x in range(3):
                    matrix[pairs[x][0]][pairs[x][1]] = matrix[pairs[x + 1][0]][pairs[x + 1][1]]
                matrix[pairs[3][0]][pairs[3][1]] = temp
