class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        0 > dead
        1 > alive
        2 > dead -> alive
        3 > alive -> dead
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                # for each cell, process the neighbours
                # subtracting this, since the point itself gets counted in the loop
                count = -1 * board[i][j]
                for x in range(max(0, i - 1), min(len(board), i + 2)):
                    for y in range(max(0, j - 1), min(len(board[0]), j + 2)):
                        count += board[x][y] % 2
                # in other cases, new = old
                if board[i][j] and (count > 3 or count < 2):
                    board[i][j] = 3
                elif not board[i][j] and count == 3:
                    board[i][j] = 2

        # convert 2,3 to 1,0 respectively
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = min(board[i][j], 3 - board[i][j])
