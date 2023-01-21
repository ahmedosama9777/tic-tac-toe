class Game():
    def __init__(self):
        self.game_board = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
    def winner(self):
        return 0
    
    def takeTurn(self, player: str, position: list):
        self.game_board[position[0]][position[1]] = player