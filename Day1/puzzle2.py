"""
Day 1: Sonar Sweep [PART 2]

Count the number of times the sum of measurements in this sliding window
increases from the previous sum.
"""
from puzzle1 import read_input, count_increases


def create_sliding_windows(input_lines: list[int],
                           group_of: int) -> list[int]:
    """Creates sliding window lists of size 'group_of'."""
    windows = []
    for i in range(len(input_lines) - (group_of - 1)):
        # Group into a list of lists:
        grouped = input_lines[i:i + group_of]
        windows.append(grouped)
    return windows


def find_list_sums(windows: list[list[int]]) -> list[int]:
    """Finds the sum of each list in a list of lists."""
    sums = []
    for window in windows:
        sums.append(sum(window))
    return sums


# Find our answer...
input_lines = read_input('Day1/day1-input.txt')
sliding_windows = create_sliding_windows(input_lines, 3)
window_sums = find_list_sums(sliding_windows)
num_increases = count_increases(window_sums)

print(f"Part Two: {num_increases} sliding window increases found.\n")
