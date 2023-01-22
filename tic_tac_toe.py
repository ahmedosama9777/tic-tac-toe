class Game:
    def __init__(self):
        self.game_board = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]

    def winner(self):
        if self._horizontal_win():
            return self._horizontal_win()
        elif self._vertical_win():
            return self._vertical_win()

        return 0

    def takeTurn(self, player: str, position: list):
        self.game_board[position[0]][position[1]] = player

    def _horizontal_win(self):
        for row in range(len(self.game_board[0])):
            if (
                self.game_board[row][0] == self.game_board[row][1]
                and self.game_board[row][0] == self.game_board[row][2]
                and self.game_board[row][0] != "0"
            ):
                return f"Player {self.game_board[row][0]} wins!"

        return 0

    def _vertical_win(self):
        for col in range(len(self.game_board)):
            if (
                self.game_board[0][col] == self.game_board[1][col]
                and self.game_board[1][col] == self.game_board[2][col]
                and self.game_board[0][col] != "0"
            ):
                return f"Player {self.game_board[0][col]} wins!"

        return 0
