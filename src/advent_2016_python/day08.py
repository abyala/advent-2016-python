import re
from typing import Dict, Tuple, Final

from advent_2016_python.utils import SOLID_BLOCK

type Screen = Dict[Tuple[int, int], bool]
MAX_WIDTH: Final[int] = 50
MAX_HEIGHT: Final[int] = 6


def initial_screen() -> Screen:
    screen = {}
    for x in range(MAX_WIDTH):
        for y in range(MAX_HEIGHT):
            screen[(x, y)] = False
    return screen


def run_command(screen: Screen, cmd: str):
    v0, v1 = list(map(int, re.findall("(\\d+)", cmd)))
    if cmd.startswith("rect"):
        screen.update({(x, y): True for x in range(v0) for y in range(v1)})
    elif cmd.startswith("rotate row y="):
        screen |= {(x, v0): screen[((x - v1) % MAX_WIDTH, v0)] for x in range(MAX_WIDTH)}
    else:
        screen |= {(v0, y): screen[(v0, (y - v1) % MAX_HEIGHT)] for y in range(MAX_HEIGHT)}


def run_all(data: str) -> Screen:
    screen = initial_screen()
    for command in data.splitlines():
        run_command(screen, command)
    return screen


def part1(data: str) -> int:
    screen = run_all(data)
    return len([v for v in screen.values() if v])


def part2(data: str):
    print()
    screen = run_all(data)
    for y in range(MAX_HEIGHT):
        print("".join([SOLID_BLOCK if screen[(x, y)] else " " for x in range(MAX_WIDTH)]))
