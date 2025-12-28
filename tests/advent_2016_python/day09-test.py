from pathlib import Path

import pytest

from advent_2016_python.day09 import part1, part2

PUZZLE_TEXT = Path("../resources/day09-puzzle.txt").read_text()


@pytest.mark.parametrize("data, expected", [("ADVENT", 6),
                                            ("A(1x5)BC", 7),
                                            ("(3x3)XYZ", 9),
                                            ("A(2x2)BCD(2x2)EFG", 11),
                                            ("(6x1)(1x3)A", 6),
                                            ("X(8x2)(3x3)ABCY", 18),
                                            (PUZZLE_TEXT, 70186)])
def test_part1(data, expected):
    assert part1(data) == expected


@pytest.mark.parametrize("data, expected", [("(3x3)XYZ", 9),
                                            ("X(8x2)(3x3)ABCY", 20),
                                            ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
                                            ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
                                            (PUZZLE_TEXT, 10915059201)])
def test_part2(data, expected):
    assert part2(data) == expected
