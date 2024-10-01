import os
import sys
import pytest

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('...'))

from typing import Dict, Tuple

from PyTestUtkin316.utils import TriangleProblemTwo
from PyTestUtkin316.enums import TriangleSidesType as sides

@pytest.mark.parametrize("data",
                         [
                             {"input": (8, 2, 3), "expected": sides.sharp_angled},
                             {"input": (4, 7, 7), "expected": sides.obtuse_angle},
                             {"input": (4, 4, 4), "expected": sides.rectangular}
                         ])
def test_triangle_sides_type(data: Dict[Tuple[float,
                                              float,
                                              float], sides]):
    o = TriangleProblemTwo()

    s = data["input"]

    ans = o.defineTriangleSides(s[0], s[1], s[2])

    assert ans == data["expected"]
