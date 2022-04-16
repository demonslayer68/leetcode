class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        The idea is to use 2^0 place to store current state and 2^1 place to store next state.
        so we do //2 for next state and %2 for current state.
        Rest is straight forward
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbours = -1 * board[i][j]
                for x in range(max(i - 1, 0), min(len(board) - 1, i + 1) + 1):
                    for y in range(max(j - 1, 0), min(len(board[0]) - 1, j + 1) + 1):
                        neighbours += board[x][y] % 2

                if ((neighbours == 2 or neighbours == 3) and board[i][j]) or (neighbours == 3 and not board[i][j]):
                    board[i][j] += 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] // 2
