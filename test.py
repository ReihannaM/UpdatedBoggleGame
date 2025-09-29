import unittest
from boggle_solver import Boggle

class TestBoggleSolver(unittest.TestCase):

    def test_basic_words(self):
        grid = [
            ["C", "A", "T"],
            ["R", "I", "O"],
            ["M", "U", "P"]
        ]
        dictionary = ["CAT", "CUP", "RUM", "TOP", "TIP"]
        game = Boggle(grid, dictionary)
        found = game.getSolution()
        expected = sorted(["CAT", "CUP", "RUM"])
        self.assertEqual(found, expected)

    def test_short_words(self):
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["AB", "AD", "ACE", "BE"]
        game = Boggle(grid, dictionary)
        found = game.getSolution()
        expected = sorted(["ACE"])
        self.assertEqual(found, expected)

    def test_empty_inputs(self):
        game = Boggle([], [])
        self.assertEqual(game.getSolution(), [])

        game = Boggle([["A"]], [])
        self.assertEqual(game.getSolution(), [])

        game = Boggle([], ["ABC"])
        self.assertEqual(game.getSolution(), [])

    def test_qu_handling(self):
        grid = [
            ["Qu", "I", "P"],
            ["U", "A", "T"],
            ["S", "T", "O"]
        ]
        dictionary = ["QUIP", "QUIT", "QUIZ", "QUA", "QAT", "Q"]
        game = Boggle(grid, dictionary)
        found = game.getSolution()
        expected = sorted(["QUIP", "QUIT", "QUA"])
        self.assertEqual(found, expected)

    def test_invalid_inputs(self):
        grid = [[1, 2], [3, 4]]  # numbers instead of strings
        dictionary = ["12", "34"]
        game = Boggle(grid, dictionary)
        found = game.getSolution()
        self.assertEqual(found, [])

    def test_duplicates(self):
        grid
