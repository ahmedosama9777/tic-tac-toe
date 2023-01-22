from unittest import TestCase

from tic_tac_toe import Game


class TestGame(TestCase):
    def setUp(self) -> None:
        self.game = Game()

    def test_game_creation(self):
        self.assertEqual(self.game.winner(), 0)

    def test_player_turn(self):
        self.game.takeTurn("X", [0, 0])
        self.assertEqual(
            self.game.game_board, [["X", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
        )

    def test_horizontal_win(self):
        self.game.game_board = [["X", "X", "X"], ["0", "0", "0"], ["0", "0", "0"]]
        self.assertEqual(self.game.winner(), "Player X wins!")

    def test_vertical_win(self):
        self.game.game_board = [["X", "0", "0"], ["X", "0", "0"], ["X", "0", "0"]]
        self.assertEqual(self.game.winner(), "Player X wins!")
