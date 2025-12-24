import pytest

from advent_2016_python.day05 import part1, part2

PUZZLE_TEXT = "cxdnnyjw"


@pytest.mark.parametrize("seed, expected", [("abc", "18f47a30"),
                                            (PUZZLE_TEXT, "f77a0e6e")])
def test_part1(seed, expected):
    assert part1(seed) == expected


@pytest.mark.parametrize("seed, expected", [("abc", "05ace8e3"),
                                            (PUZZLE_TEXT, "999828ec")])
def test_part2(seed, expected):
    assert part2(seed) == expected
