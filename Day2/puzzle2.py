"""
Day 2: Dive! [PART 2]

Using this new interpretation of the commands, calculate the horizontal
position and depth you would have after following the planned course.

Question: What do you get if you multiply your final horizontal position
by your final depth?
"""
from puzzle1 import parse_input


def calc_with_aim(data: list[tuple]) -> dict:
    """Calculate submarine's position with the third tracking value: aim.

    Conditions:
    - down X increases your aim by X units.
    - up X decreases your aim by X units.
    - forward X does two things:
        + It increases your horizontal position by X units.
        + It increases your depth by your aim multiplied by X.

    Returns
    -------
    dict: {'depth': int, 'hpos': int}
        The resulting depth and horizontal position after taking
        in the aim factor.
    """
    # Initialize our params:
    aim, depth, hpos = 0, 0, 0

    # Iterate through each tuple:
    for direction, value in data:
        if direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
        elif direction == 'forward':
            hpos += value
            depth += aim * value

    return {'depth': depth, 'hpos': hpos}


# Find our answer...
parsed_input = parse_input('Day2/day2-input.txt')
calculated_with_aim = calc_with_aim(parsed_input)
depth = calculated_with_aim['depth']
hpos = calculated_with_aim['hpos']

print(f"Part Two: {depth} depth x {hpos} hpos = {depth * hpos}")
