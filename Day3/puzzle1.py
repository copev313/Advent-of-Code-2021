"""
Day 3: Binary Diagnostic [PART 1]

Use the binary numbers in your diagnostic report to calculate the gamma rate
and epsilon rate, then multiply them together.

Question: What is the power consumption of the submarine? (Be sure to
represent your answer in decimal, not binary.)
"""


def read_binary_input(filepath: str) -> list[str]:
    """Reads binary input from a file and returns a list of binary
    values.
    """
    with open(filepath, 'r') as file:
        lines = file.readlines()
        # Remove newline characters:
        return [line.strip().replace('\n', '') for line in lines]


def find_gamma_rate(binary_input: list[str]) -> str:
    """Finds the gamma rate from the binary input.

    Gamma rate is calculated as the most common value for a given bit
    position.

    Returns
    -------
    str
        The gamma rate as a binary string.
    """
    # Init a string to append to later:
    gamma_rate = '0b'
    # Grab the length of a value from the list:
    value_length = len(binary_input[0])

    # Iterate through the bit positions:
    for i in range(value_length):
        num_ones, num_zeroes = 0, 0

        # Iterate through the list of values:
        for value in binary_input:
            if value[i] == '1':
                num_ones += 1
            elif value[i] == '0':
                num_zeroes += 1

        # Determine which value is most common:
        if num_ones > num_zeroes:
            gamma_rate += '1'
        else:
            gamma_rate += '0'

    return gamma_rate


def find_epsilon_rate(binary_gamma_rate: str) -> str:
    """Finds the epsilon rate, given the gamma rate (as a binary string).

    Epsilon rate is calculated as the least common value for a given bit
    position.

    Returns
    -------
    str
        The epsilon rate as a binary string.
    """
    # Remove '0b' prefix from the binary string:
    bin_gamma = binary_gamma_rate.replace('0b', '')
    epsilon_rate = '0b'

    for i in range(len(bin_gamma)):
        if bin_gamma[i] == '1':
            epsilon_rate += '0'
        else:
            epsilon_rate += '1'

    return epsilon_rate


# Find our answer...
input_list = read_binary_input('Day3/day3-input.txt')

bin_gamma = find_gamma_rate(input_list)  # 0b000110001010
gamma = int(bin_gamma, 2)                # 394

bin_epsilon = find_epsilon_rate(bin_gamma)  # 0b111001110101
epsilon = int(bin_epsilon, 2)               # 3701

# Print our results to the console:
print("\nDAY 3\n-----")
print("Part One:")
print(f"Gamma binary: {bin_gamma}")
print(f"Epsilon binary: {bin_epsilon}")
print("Power consumption: gamma_rate x epsilon_rate = "
      f"{gamma} x {epsilon} = {gamma * epsilon}")
