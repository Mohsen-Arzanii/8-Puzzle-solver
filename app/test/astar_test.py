import unittest
from core.astar import manhattan_dist, astar
from model import Puzzle

class TestManhattanDistance(unittest.TestCase):
    def test_manhattan_calculation(self):
        # 7, 2, 4, 5, 0, 6, 8, 3, 1
        p = Puzzle('64785X321')
        manhattan = manhattan_dist(p) 
        must_be = 21 
        self.assertEqual(manhattan, must_be)

    def test_path_finding(self):
        p = Puzzle('8672543X1')
        solvable, data = astar(p)



