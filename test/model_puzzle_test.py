import unittest
from model import Puzzle

class TestPuzzleModel(unittest.TestCase):
    def test_generate_states(self):
        state = Puzzle('12345678X')
        possible_states = state.generate_states()
        must_be = [Puzzle('12345X786'), Puzzle('1234567X8')]

        self.assertCountEqual(possible_states, must_be)

    def test_invalid_states(self):
        state1 = Puzzle('12345')
        with self.assertRaises(ValueError):
            state1.generate_states()

        state2 = Puzzle('123456789')
        with self.assertRaises(ValueError):
            state2.generate_states()

