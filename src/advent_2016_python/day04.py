import re
from collections import Counter
from typing import Tuple

type Room = Tuple[str, int, str]
A_ORD: int = ord("a")


def parse_room(s: str) -> Room:
    _, name, id, checksum, _ = re.split(r'(.*)-(\d+)\[(\w*)', s)
    return name, int(id), checksum


def is_real_room(room: Room) -> bool:
    name, _, checksum = room
    frequencies = Counter(name.replace("-", ""))
    return checksum == "".join(i[0] for i in sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))[0:5])


def part1(data: str) -> int:
    return sum(r[1] for r in [parse_room(line) for line in data.splitlines()] if is_real_room(r))


def rotate(room: Room):
    name, id, _ = room
    return "".join(" " if c == "-" else chr(((ord(c) + (id % 26) - A_ORD) % 26) + A_ORD) for c in name)


def part2(data: str) -> int:
    return next(room[1] for room in [parse_room(s) for s in data.splitlines()]
                if rotate(room) == "northpole object storage")
