# run this file to check all tests
# eg. python run_tests.py
# if yout wrote a new test and want to run, import your test to this file

import unittest
import pathlib
import sys
# append parent directory to PATH
parent = (pathlib.Path(__file__).resolve().parents[1])
sys.path.append(str(parent))

# import your tests here
from model_puzzle_test import TestPuzzleModel
from util_test import TestUtilShapeShift, TestUtilGetPath
from ids_test import TestIds, TestDfs
from astar_test import TestManhattanDistance 

if __name__ == '__main__':
    unittest.main()
