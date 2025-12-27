from pathlib import Path

from advent_2016_python.day08 import part1, part2

PUZZLE_TEXT = Path("../resources/day08-puzzle.txt").read_text()


def test_part1():
    assert part1(PUZZLE_TEXT) == 121


def test_part2():
    # No assertions... just printing
    part2(PUZZLE_TEXT)
