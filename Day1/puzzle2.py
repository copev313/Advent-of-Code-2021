"""
Day 1: Sonar Sweep [PART 2]

Count the number of times the sum of measurements in this sliding window
increases from the previous sum.
"""
from puzzle1 import read_input, count_increases


def create_sliding_windows(input_lines: list[int],
                           group_of: int) -> list[int]:
    """Creates sliding window lists of size 'group_of'. """
    # Define our range of indices:
    range_span = range(len(input_lines) - (group_of - 1))
    # Create a list of sublists using a list comprehension:
    windows = [input_lines[i:i + group_of] for i in range_span]
    return windows


def find_list_sums(windows_list: list[list[int]]) -> list[int]:
    """Finds the sum of each list in a list of lists. """
    return [sum(window) for window in windows_list]


# Find our answer...
input_lines = read_input('Day1/day1-input.txt')
sliding_windows = create_sliding_windows(input_lines, 3)
window_sums = find_list_sums(sliding_windows)
num_increases = count_increases(window_sums)

print(f"Part Two: {num_increases} sliding window increases found.\n")
