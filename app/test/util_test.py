import unittest
from core import util
from model import Puzzle

class TestUtilShapeShift(unittest.TestCase): 
    def test_simple_input(self):
        strings = ['12345X786', '12345678X']
        data = util.shapeshift(strings)
        must_be = [
                [{'val': '1', 'attrib': 'correct item1'},
                 {'val': '2', 'attrib': 'correct item2'},
                 {'val': '3', 'attrib': 'correct item3'},
                 {'val': '4', 'attrib': 'correct item4'},
                 {'val': '5', 'attrib': 'correct item5'},
                 {'val': 'X', 'attrib': 'empty'},
                 {'val': '7', 'attrib': 'correct item7'},
                 {'val': '8', 'attrib': 'correct item8'},
                 {'val': '6', 'attrib': 'correct item6'},
                 ],
                [{'val': '1', 'attrib': 'correct item1'},
                 {'val': '2', 'attrib': 'correct item2'},
                 {'val': '3', 'attrib': 'correct item3'},
                 {'val': '4', 'attrib': 'correct item4'},
                 {'val': '5', 'attrib': 'correct item5'},
                 {'val': '6', 'attrib': 'correct item6'},
                 {'val': '7', 'attrib': 'correct item7'},
                 {'val': '8', 'attrib': 'correct item8'},
                 {'val': 'X', 'attrib': 'empty'},
                 ]
                ]

        self.assertListEqual(data, must_be)


class TestUtilGetPath(unittest.TestCase): 
    def test_path(self):
        parent = {'12345678X': '1234567X8'}
        data = util.getpath('12345678X', parent)
        must_be = ['1234567X8', '12345678X']
        self.assertListEqual(data, must_be)

