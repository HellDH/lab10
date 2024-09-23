import os
import sys

parent_directory = os.path.abspath('..')

sys.path.append(parent_directory)

from PyTestUtkin316.utils import TriangleProblemOne

def test_scalene():
    o = TriangleProblemOne()
    ans = o.defineTriangle(1, 2, 3)
    assert ans == 1.0

def test_isosceles():
    o = TriangleProblemOne()
    ans = o.defineTriangle(4, 2, 2)
    assert ans == 1.0

def test_equilateral():
    o = TriangleProblemOne()
    ans = o.defineTriangle(4, 4, 4)
    assert ans == 0.5
