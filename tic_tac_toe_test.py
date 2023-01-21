from unittest import TestCase

from tic_tac_toe import Game

class TestGame(TestCase):
    def test_game_creation(self):
        game = Game()
        self.assertEqual(game.winner(), 0)