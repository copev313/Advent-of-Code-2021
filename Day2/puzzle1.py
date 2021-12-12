"""
Day 2: Dive! [PART 1]

Calculate the horizontal position and depth you would have after
following the planned course.

Question: What do you get if you multiply your final horizontal position by
your final depth?
"""


def parse_input(filename: str) -> list[tuple]:
    """Parses the input file and return a list of
    (direction, value) tuples.
    """
    parsed_list = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            splitted = line.strip().split(' ', maxsplit=1)
            dir_part = splitted[0]
            val_part = int(splitted[1])
            parsed_list.append((dir_part, val_part))

    return parsed_list


def get_depth(data: list[tuple]) -> int:
    """Returns the depth of the submarine."""
    depth = 0
    for direction, value in data:
        if direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value
        else:
            continue

    return depth


def get_horizontal_position(data: list[tuple]) -> int:
    """Returns the horizontal position of the submarine."""
    hpos = 0
    for direction, value in data:
        if direction == 'forward':
            hpos += value

    return hpos


# Find our answer...
parsed_input = parse_input('Day2/input.txt')
depth = get_depth(parsed_input)
hpos = get_horizontal_position(parsed_input)

print("\nDAY 2\n-----")
print(f"Part One: {depth} depth x {hpos} hpos = {depth * hpos}")
