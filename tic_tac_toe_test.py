from unittest import TestCase

from tic_tac_toe import Game

class TestGame(TestCase):
    def test_game_creation(self):
        game = Game()
        self.assertEqual(game.winner(), 0)
    
    def test_player_turn(self):
        game = Game()
        game.takeTurn("X", [0, 0])
        self.assertEqual(game.game_board, [["X", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]])