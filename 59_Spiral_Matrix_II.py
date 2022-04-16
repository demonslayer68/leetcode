class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0 for _ in range(n)] for _ in range(n)]
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        direction = 0
        number = 1
        row = col = 0
        lower = -1
        upper = n
        while number <= n ** 2:
            output[row][col] = number
            if row == lower + 2 and col == lower + 1:
                lower += 1
                upper -= 1
            if row + directions[direction][0] == lower or row + directions[direction][0] == upper or col + directions[direction][1] == lower or col + directions[direction][1] == upper:
                direction = (direction + 1) % 4
            row += directions[direction][0]
            col += directions[direction][1]
            number += 1
        return output