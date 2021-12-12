"""
Day 1: Sonar Sweep [PART 1]

Question: How many measurements are larger than the previous measurement?
"""

def read_input(filename: str) -> list[int]:
    """Accepts a input file name and returns a list of integers."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        return list(map(int, lines))


def count_increases(input_list: list[int]) -> int:
    """Takes a list of integers and returns the number of times an increase
    occurs.
    """
    count = 0
    for i, val in enumerate(input_list):
        if i == 0:
            continue
        if val > input_list[i - 1]:
            count += 1

    return count


# Find out answer...
input_lines = read_input('Day1/day1-input.txt')
num_increases = count_increases(input_lines)

print("\nDAY 1\n-----")
print(f"Part One: {num_increases} increases found.")
