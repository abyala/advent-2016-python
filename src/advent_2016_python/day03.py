from itertools import batched
from typing import List, Tuple, Callable

type NumberList = List[int]


def is_triangle(sides: Tuple[int, int, int]) -> bool:
    a, b, c = sorted(sides)
    return a + b > c


def parse_nums(data: str) -> NumberList:
    return list(int(v) for v in data.split())


def flip(nums: NumberList) -> NumberList:
    n1, n2, n3 = [], [], []
    for batch in batched(nums, 3):
        n1.append(batch[0])
        n2.append(batch[1])
        n3.append(batch[2])
    return n1 + n2 + n3


def solve(xf: Callable[[NumberList], NumberList], data: str) -> int:
    triples = list(batched(xf(parse_nums(data)), 3))
    return sum(1 for t in triples if is_triangle(t))


def part1(data: str) -> int:
    return solve(lambda x: x, data)


def part2(data: str) -> int:
    return solve(flip, data)
