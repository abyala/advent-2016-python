from pathlib import Path

import pytest

from advent_2016_python.day07 import supports_tls, supports_ssl, part1, part2

PUZZLE_TEXT = Path("../resources/day07-puzzle.txt").read_text()


@pytest.mark.parametrize("s, expected", [("abba[mnop]qrst", True),
                                         ("abcd[bddb]xyyx", False),
                                         ("aaa[qwer]tyui", False),
                                         ("ioxxoj[asdfgh]zxcvbn", True)])
def test_supports_tls(s, expected):
    assert supports_tls(s) == expected


def test_part1():
    assert part1(PUZZLE_TEXT) == 110


@pytest.mark.parametrize("s, expected", [("aba[bab]xyz", True),
                                         ("xyx[xyx]xyx", False),
                                         ("aaa[kek]eke", True),
                                         ("zazbz[bzb]cdb", True)])
def test_supports_ssl(s, expected):
    assert supports_ssl(s) == expected


def test_part2():
    assert part2(PUZZLE_TEXT) == 242
