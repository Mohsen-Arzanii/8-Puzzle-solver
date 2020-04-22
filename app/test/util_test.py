import unittest
from core import util

class TestUtilShapeShift(unittest.TestCase): 
    def test_simple_input(self):
        strings = ['12345X786', '12345678X']
        data = util.shapeshift(strings)
        must_be = [
                [{'val': '1', 'attrib': 'correct'},
                 {'val': '2', 'attrib': 'correct'},
                 {'val': '3', 'attrib': 'correct'},
                 {'val': '4', 'attrib': 'correct'},
                 {'val': '5', 'attrib': 'correct'},
                 {'val': 'X', 'attrib': 'empty'},
                 {'val': '7', 'attrib': 'correct'},
                 {'val': '8', 'attrib': 'correct'},
                 {'val': '6', 'attrib': 'correct'},
                 ],
                [{'val': '1', 'attrib': 'correct'},
                 {'val': '2', 'attrib': 'correct'},
                 {'val': '3', 'attrib': 'correct'},
                 {'val': '4', 'attrib': 'correct'},
                 {'val': '5', 'attrib': 'correct'},
                 {'val': '6', 'attrib': 'correct'},
                 {'val': '7', 'attrib': 'correct'},
                 {'val': '8', 'attrib': 'correct'},
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

