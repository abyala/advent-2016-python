import itertools
import re
from typing import List, Tuple, Callable

type IpPattern = (Callable[[str], bool], int)

ABBA_PATTERN: IpPattern = (lambda s: len(s) == 4 and s[0] == s[3] and s[1] == s[2] and s[0] != s[1], 4)
ABA_PATTERN: IpPattern = (lambda s: len(s) == 3 and s[0] == s[2] and s[0] != s[1], 3)


def split_ip(ip: str) -> Tuple[List[str], List[str]]:
    supernets = []
    hypernets = []
    remaining = ip
    while True:
        tokens = re.split('([^\\[]*)\\[([^]]*)](.*)', remaining)
        if len(tokens) == 1:
            if len(tokens[0]) >= 3:
                supernets.append(tokens[0])
            return supernets, hypernets
        else:
            _, before, within, after, _ = tokens
            if len(before) >= 3:
                supernets.append(before)
            if len(within) >= 3:
                hypernets.append(within)
            remaining = after


def all_of_pattern(pattern: IpPattern, ss: List[str]) -> List[str]:
    fn, n = pattern

    def find(s: str) -> List[str]:
        return [s[i:i + n] for i in range(len(s) - n + 1) if fn(s[i:i + n])]

    return list(itertools.chain.from_iterable(map(find, ss)))


def supports_tls(ip):
    supers, hypers = split_ip(ip)
    return len(all_of_pattern(ABBA_PATTERN, supers)) > 0 and len(all_of_pattern(ABBA_PATTERN, hypers)) == 0


def supports_ssl(ip):
    supers, hypers = list(map(lambda grp: set(all_of_pattern(ABA_PATTERN, grp)), split_ip(ip)))
    return any(map(lambda s: f"{s[1]}{s[0]}{s[1]}" in hypers, supers))


def solve(fn: Callable[[str], bool], data: str) -> int:
    return len(list(filter(fn, data.splitlines())))


def part1(data: str) -> int:
    return solve(supports_tls, data)


def part2(data: str) -> int:
    return solve(supports_ssl, data)
