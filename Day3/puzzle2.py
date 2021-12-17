"""
Day 3: Binary Diagnostic [PART 2]

Use the binary numbers in your diagnostic report to calculate the oxygen
generator rating and CO2 scrubber rating, then multiply them together.

Question: What is the life support rating of the submarine?
"""
# from pprint import pprint
from puzzle1 import read_binary_input


def oxygen_generator_rating(binary_input: list[str]) -> str:
    """Finds the oxygen generator rating.

    To find oxygen generator rating, determine the MOST COMMON value (0 or 1)
    in the current bit position, and keep only numbers with that bit in that
    position. If 0 and 1 are equally common, keep values with a 1 in the
    position being considered.

    Returns
    -------
    str
        The binary string representing the oxygen generator rating.
    """
    # Iterate through the bit positions:
    for i in range(len(binary_input[0])):
        values_with_1s, values_with_0s = [], []

        # Iterate through the list of values:
        for value in binary_input:
            if value[i] == '1':
                values_with_1s.append(value)
            else:
                values_with_0s.append(value)

        # Determine which value is most common:
        # [CASE] More ones than zeroes, or equally common:
        if len(values_with_1s) >= len(values_with_0s):
            binary_input = values_with_1s
        else:
            binary_input = values_with_0s

        # End condition:
        if len(binary_input) == 1:
            break

    return f"0b{binary_input[0]}"


def co2_scrubber_rating(binary_input: list[str]) -> str:
    """Finds the CO2 scrubber rating.

    To find CO2 scrubber rating, determine the LEAST COMMON value (0 or 1) in
    the current bit position, and keep only numbers with that bit in that
    position. If 0 and 1 are equally common, keep values with a 0 in the
    position being considered.

    Returns
    -------
    str
        The binary string representing the CO2 scrubber rating.
    """
    # Iterate through each bit position:
    for i in range(len(binary_input[0])):
        values_with_1s, values_with_0s = [], []

        # Iterate through the list of values:
        for value in binary_input:
            if value[i] == '1':
                values_with_1s.append(value)
            else:
                values_with_0s.append(value)

        # Determine which value is least common:
        # [CASE] More zeros than ones, or equally common:
        if len(values_with_1s) >= len(values_with_0s):
            binary_input = values_with_0s
        else:
            binary_input = values_with_1s

        # End condition:
        if len(binary_input) == 1:
            break

    return f"0b{binary_input[0]}"


# Find our answer...
input_list = read_binary_input('Day3/day3-input.txt')
oxy_rating = oxygen_generator_rating(input_list)    # 0b001100010101 -> 789
co2_rating = co2_scrubber_rating(input_list)        # 0b001100010000 -> 3586


# Print our results to the console:
print("\nPart Two: ")
print(f"Oxygen Generator Rating: {oxy_rating} -> {int(oxy_rating, 2)}")
print(f"CO2 Scrubber Rating: {co2_rating} -> {int(co2_rating, 2)}")
print(f"Life Support Rating: {int(oxy_rating, 2)} x {int(co2_rating, 2)} = "
      f"{int(oxy_rating, 2) * int(co2_rating, 2)}")
