import pytest

from pathlib import Path
from advent_2016_python.day01 import part1, part2

puzzle_text = Path("../resources/day01-puzzle.txt").read_text()

@pytest.mark.parametrize("s, expected", [("R2, L3", 5),
                                         ("R2, R2, R2", 2),
                                         ("R5, L5, R5, R3", 12),
                                         (puzzle_text, 252)])
def test_part1(s, expected):
    assert part1(s) == expected

@pytest.mark.parametrize("s, expected", [("R8, R4, R4, R8", 4),
                                         (puzzle_text, 143)])
def test_part2(s, expected):
    assert part2(s) == expected
