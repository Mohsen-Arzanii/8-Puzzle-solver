import unittest
from core.ids import ids, dfs_with_limit
from model import Puzzle

class TestDfs(unittest.TestCase):
    def test_found_answer(self):
        p = Puzzle('1234567X8')
        last_item = dfs_with_limit(p, 10)
        must_be = '12345678X'
        self.assertEqual(last_item, must_be)

    def test_not_found(self):
        # a limit with less value might be lead to not 'found'
        p = Puzzle('123456X78')
        data = dfs_with_limit(p, 1) # limit is zero
        self.assertEqual(data, None)


class TestIds(unittest.TestCase): 
    def test_not_solvable(self):
        p = Puzzle('812X43765')
        solvable, numofnodes,res = ids(p)
        self.assertFalse(solvable)

    def test_found_answer(self):
        p1 = Puzzle('1234567X8')
        solvable, numofnodes, data = ids(p1)
        must_be = (True, Puzzle('12345678X'))
        self.assertEqual((solvable, data[-1]), must_be)

        p2 = Puzzle('X13425786')
        solvable, numofnodes, data = ids(p2)
        must_be = (True, Puzzle('12345678X'))
        self.assertEqual((solvable, data[-1]), must_be)

    def test_hardest_case(self):
        p1 = Puzzle('8672543X1')
        solvable, numofnodes, data = ids(p1)
        must_be = (True, Puzzle('12345678X'))
        self.assertEqual((solvable, data[-1]), must_be)

