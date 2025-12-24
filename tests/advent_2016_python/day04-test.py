from pathlib import Path

from advent_2016_python.day04 import part1, part2

puzzle_text = Path("../resources/day04-puzzle.txt").read_text()


def test_part1():
    assert part1(puzzle_text) == 245102


def test_part2():
    assert part2(puzzle_text) == 324
