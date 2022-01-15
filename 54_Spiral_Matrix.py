class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        dirn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        bounds = [len(matrix[0]), len(matrix), -1, 0]
        output = []
        i = 0
        j = 0
        x = 0
        while len(output) < len(matrix) * len(matrix[0]):
            output.append(matrix[i][j])
            i += dirn[x][0]
            j += dirn[x][1]
            if (dirn[x][0] and i == bounds[x]) or (dirn[x][1] and j == bounds[x]):
                i -= dirn[x][0]
                j -= dirn[x][1]
                bounds[x] -= sum(dirn[x])
                x = (x + 1) % 4
                i += dirn[x][0]
                j += dirn[x][1]
        return output

