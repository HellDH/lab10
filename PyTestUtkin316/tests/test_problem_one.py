import os
import sys
import pytest

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('...'))

from typing import Dict, Tuple
from PyTestUtkin316.utils import TriangleProblemOne

@pytest.mark.parametrize("data",
                         [
                             {"input": (1, 2, 3), "expected": 1},
                             {"input": (4, 2, 2), "expected": 1},
                             {"input": (4, 4, 4), "expected": 0.5}
                         ])
def test_triangle_type(data: Dict[Tuple[int|float,
                                  int|float,
                                  int|float], int]):
    o = TriangleProblemOne()

    s = data["input"]

    ans = o.defineTriangle(s[0], s[1], s[2])

    assert ans[0] == data["expected"]
