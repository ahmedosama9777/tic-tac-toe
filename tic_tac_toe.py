class Game:
    def __init__(self):
        self.game_board = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]

    def winner(self):
        for row in range(len(self.game_board[0])):
            if (
                self.game_board[row][0] == self.game_board[row][1]
                and self.game_board[row][0] == self.game_board[row][2]
                and self.game_board[row][0] != "0"
            ):
                return f"Player {self.game_board[row][0]} wins!"
        return 0

    def takeTurn(self, player: str, position: list):
        self.game_board[position[0]][position[1]] = player
