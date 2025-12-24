from pathlib import Path

import pytest

from advent_2016_python.day06 import part1, part2

TEST_TEXT = Path("../resources/day06-test.txt").read_text()
PUZZLE_TEXT = Path("../resources/day06-puzzle.txt").read_text()


@pytest.mark.parametrize("seed, expected", [(TEST_TEXT, "easter"),
                                            (PUZZLE_TEXT, "gebzfnbt")])
def test_part1(seed, expected):
    assert part1(seed) == expected


@pytest.mark.parametrize("seed, expected", [(TEST_TEXT, "advent"),
                                            (PUZZLE_TEXT, "fykjtwyn")])
def test_part2(seed, expected):
    assert part2(seed) == expected
