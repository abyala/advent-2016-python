import re
from typing import Final

PATTERN: Final[str] = "([^\\(]*)\\((\\d+)x(\\d+)\\)(.*)"


def solve(is_nested: bool, s: str) -> int:
    try:
        _, before, num_chars, repeats, after, _ = re.split(PATTERN, s)
        idx_low = len(before) + 3 + len(num_chars) + len(repeats)
        idx_high = idx_low + int(num_chars)
        if is_nested:
            middle = solve(is_nested, s[idx_low:idx_high])
        else:
            middle = int(num_chars)
        return len(before) + middle * int(repeats) + solve(is_nested, s[idx_high:])
    except ValueError:
        return len(s)


def part1(s):
    return solve(False, s)


def part2(s):
    return solve(True, s)
