from collections import Counter


def solve(target_idx: int, data: str) -> str:
    words = data.splitlines()
    return "".join(
        sorted(Counter(w[i] for w in words).items(),
               key=lambda item: item[1])[target_idx][0]
        for i in range(len(words[0])))


def part1(data: str) -> str:
    return solve(-1, data)


def part2(data: str) -> str:
    return solve(0, data)
