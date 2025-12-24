import hashlib
from itertools import count, islice
from typing import Iterator


def md5(s: str) -> str:
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def is_password(s: str) -> bool:
    return s.startswith("00000")


def interesting_hash_seq(seed: str) -> Iterator[str]:
    for i in count():
        h = md5(f"{seed}{i}")
        if is_password(h):
            yield h[5:]


def part1(data: str) -> str:
    return "".join(s[0] for s in islice(interesting_hash_seq(data), 8))


def part2(data: str) -> str:
    password = {}
    for s in interesting_hash_seq(data):
        idx, c = s[0:2]
        if "0" <= idx <= "7" and idx not in password:
            password[idx] = c
            if len(password) == 8:
                return "".join(item[1] for item in sorted(password.items()))
    else:
        raise ValueError(f"Unable to find password for door ID {data}")
