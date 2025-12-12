import unittest
import sys
from boggle_solver import Boggle

# Must be at top to avoid E402
sys.path.append("/home/codio/workspace/")


# ================================================================
# Category: Normal Inputs + 3x3 baseline
# ================================================================
class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    def test_Normal_case_3x3(self):
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        game = Boggle(grid, dictionary)

        solution = sorted([w.upper() for w in game.getSolution()])
        expected = sorted(["ABC", "ABDHI", "CFI", "DEA"])

        self.assertEqual(expected, solution)


# ================================================================
# Category: Input Edge Cases
# ================================================================
class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    def test_1x1_grid(self):
        grid = [["A"]]
        dictionary = ["A", "B", "C"]
        game = Boggle(grid, dictionary)

        self.assertEqual([], game.getSolution())

    def test_empty_grid(self):
        grid = [[]]
        dictionary = ["HELLO", "THERE"]
        game = Boggle(grid, dictionary)

        self.assertEqual([], game.getSolution())

    def test_empty_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        game = Boggle(grid, dictionary)

        self.assertEqual([], game.getSolution())

    def test_short_words_only(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["AB", "CD", "EF"]
        game = Boggle(grid, dictionary)

        self.assertEqual([], game.getSolution())


# ================================================================
# Category: Complete 4x4 Complex Coverage
# ================================================================
class TestSuite_Complete_Coverage(unittest.TestCase):

    def test_standard_4x4_board(self):
        grid = [
            ["Qu", "A", "T", "S"],
            ["E", "R", "I", "O"],
            ["N", "L", "St", "P"],
            ["M", "U", "C", "K"]
        ]

        dictionary = [
            "QUAIL", "QUIET", "TRIO", "CUP",
            "STORM", "MOP", "STICK", "RUM",
            "TAR", "QUIP"
        ]

        game = Boggle(grid, dictionary)
        solution = game.getSolution()

        expected_present = {
            "QUAIL", "QUIET", "TRIO", "CUP",
            "MOP", "RUM", "TAR", "QUIP"
        }

        for word in expected_present:
            self.assertIn(word, solution)

        self.assertNotIn("STORM", solution)


# ================================================================
# Category: Special Tiles - QU and ST
# ================================================================
class TestSuite_Qu_and_St(unittest.TestCase):

    def test_qu_words(self):
        grid = [["Qu", "A"], ["I", "L"]]
        dictionary = ["QUAIL", "QUIT", "QUA"]
        game = Boggle(grid, dictionary)

        solution = game.getSolution()

        self.assertIn("QUAIL", solution)
        self.assertIn("QUIT", solution)
        self.assertNotIn("QUA", solution)

    def test_st_words(self):
        grid = [["St", "O"], ["P", "M"]]
        dictionary = ["STOP", "STOMP", "STO"]
        game = Boggle(grid, dictionary)

        solution = game.getSolution()

        self.assertIn("STOP", solution)
        self.assertIn("STOMP", solution)
        self.assertNotIn("STO", solution)


# ================================================================
# Category: Larger Grid / Scalability
# ================================================================
class TestSuite_Large_Grid(unittest.TestCase):

    def test_5x5_grid(self):
        grid = [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O"],
            ["P", "Q", "R", "S", "T"],
            ["U", "V", "W", "X", "Y"]
        ]

        dictionary = ["ACE", "FGL", "LMN", "STY", "XYZ"]
        game = Boggle(grid, dictionary)

        solution = game.getSolution()
        expected = []   # none of these exist in valid Boggle adjacency

        self.assertEqual(sorted(solution), sorted(expected))
