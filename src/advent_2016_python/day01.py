from advent_2016_python.point import NORTH, ORIGIN, turn

def follow_path(data):
    d = NORTH
    pos = ORIGIN
    yield pos

    for step in data.split(", "):
        d = turn("L", "R", d, step[0])
        for p in pos.path(d, int(step[1:])):
            yield p
            pos = p

def distance(p):
    return abs(p.x) + abs(p.y)

def part1(data):
    return distance(list(follow_path(data))[-1])

def part2(data):
    seen = set()
    for p in follow_path(data):
        if p in seen:
            return distance(p)
        else:
            seen.add(p)
    return -1
