class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def path(self, other, num_steps: int):
        if num_steps < 0:
            raise ValueError("num_steps argument must be a non-negative integer")

        p = self
        for _ in range(num_steps):
            p += other
            yield p


ORIGIN = Point(0, 0)
NORTH = Point(0, -1)
SOUTH = Point(0, 1)
EAST = Point(1, 0, )
WEST = Point(-1, 0)

def turn_left(facing):
    return {
        NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH
    }.get(facing)


def turn_right(facing):
    return {
        NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH
    }.get(facing)


def turn(match_left: str, match_right: str, facing: Point, direction: str):
    if direction == match_left:
        return turn_left(facing)
    elif direction == match_right:
        return turn_right(facing)
    else:
        raise ValueError("direction argument must equal either match_left or match_right arguments")
