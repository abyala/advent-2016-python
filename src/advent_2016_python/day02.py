from advent_2016_python.point import Point, NORTH, WEST, SOUTH, EAST

BASIC_KEYPAD = {
    Point(0, 0): "1", Point(1, 0): "2", Point(2, 0): "3",
    Point(0, 1): "4", Point(1, 1): "5", Point(2, 1): "6",
    Point(0, 2): "7", Point(1, 2): "8", Point(2, 2): "9"
}

BATHROOM_KEYPAD = {
    Point(2, 0): "1",
    Point(1, 1): "2", Point(2, 1): "3", Point(3, 1): "4",
    Point(0, 2): "5", Point(1, 2): "6", Point(2, 2): "7", Point(3, 2): "8", Point(4, 2): "9",
    Point(1, 3): "A", Point(2, 3): "B", Point(3, 3): "C",
    Point(2, 4): "D"
}

def find_key(keypad, n):
    return next(coords for coords in keypad.keys() if keypad[coords] == n)

def step_dir(c):
    match c:
        case "U": return NORTH
        case "D": return SOUTH
        case "L": return WEST
        case "R": return EAST
    return NotImplemented

def follow_instructions(keypad, start: Point, instructions):
    key = start
    for c in instructions:
        next_key = key + step_dir(c)
        key = next_key if next_key in keypad else key

    return key

def solve(keypad, data):
    result = ""
    pos = find_key(keypad, "5")
    for line in data.splitlines():
        new_pos = follow_instructions(keypad, pos, line)
        result += keypad[new_pos]
        pos = new_pos
    return result

def part1(data):
    return solve(BASIC_KEYPAD, data)

def part2(data):
    return solve(BATHROOM_KEYPAD, data)