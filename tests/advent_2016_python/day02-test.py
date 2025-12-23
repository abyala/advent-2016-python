import pytest

from pathlib import Path
from advent_2016_python.day02 import part1, part2

test_txt = Path("../resources/day02-test.txt").read_text()
puzzle_text = Path("../resources/day02-puzzle.txt").read_text()


@pytest.mark.parametrize("s, expected", [(test_txt, "1985"),
                                         (puzzle_text, "74921")])
def test_part1(s, expected):
    assert part1(s) == expected


@pytest.mark.parametrize("s, expected", [(test_txt, "5DB3"),
                                         (puzzle_text, "A6B35")])
def test_part2(s, expected):
    assert part2(s) == expected
