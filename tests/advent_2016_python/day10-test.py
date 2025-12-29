from pathlib import Path

import pytest

from advent_2016_python.day10 import part1, part2

TEST_TEXT = Path("../resources/day10-test.txt").read_text()
PUZZLE_TEXT = Path("../resources/day10-puzzle.txt").read_text()


@pytest.mark.parametrize("data, v0, v1, expected", [(TEST_TEXT, 2, 5, 2),
                                                    (PUZZLE_TEXT, 61, 17, 56)])
def test_part1(data, v0, v1, expected):
    assert part1(data, v0, v1) == str(expected)


@pytest.mark.parametrize("data, expected", [(TEST_TEXT, 30),
                                            (PUZZLE_TEXT, 7847)])
def test_part2(data, expected):
    assert part2(data) == expected
