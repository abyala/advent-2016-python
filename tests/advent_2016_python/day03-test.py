from pathlib import Path

from advent_2016_python.day03 import part1, part2

puzzle_text = Path("../resources/day03-puzzle.txt").read_text()

def test_part1():
    assert part1(puzzle_text) == 993


def test_part2():
    assert part2(puzzle_text) == 1849
