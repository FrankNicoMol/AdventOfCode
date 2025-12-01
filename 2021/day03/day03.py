import numpy as np
import os


def get_day_number():
    """Obtain day number from filename."""

    filename = os.path.basename(__file__)
    no_extension = filename.split(".")[0]
    day_number = no_extension[-2:]
    day_integer = int(day_number)

    return day_integer


def print_header(year=2021):
    """Print header of solutions."""

    day = get_day_number()
    print(f'\nResult of Advent of Code, year {year}, day {day}')
    print(f'Find description at https://adventofcode.com/{year}/day/{day}\n')


def load_input(input_file):
    """Read the input file and return a list"""

    with open(f'input/{input_file}', 'r') as file:
        text = file.read().strip().splitlines()

    return text


def get_bit(x, gamma=True):
    """Calculate bit gamma or epsilon code."""

    xlen = len(x)
    if gamma:
        bit = int(x.sum() > xlen // 2)
    else:
        bit = int(x.sum() < xlen // 2)
    return bit


def get_oxygen_co2(codes, oxygen=True):
    """Get oxygen or co2 values from codes."""

    n_bits = codes.shape[1]

    new_codes = np.copy(codes)
    for i in range(n_bits):
        mask = new_codes[:, i]
        if len(mask) == 1:
            break

        zeros = np.count_nonzero(mask == 0)
        ones = np.count_nonzero(mask)

        if oxygen:
            if zeros > ones:
                mask = np.logical_not(mask).astype(int)
        else:
            if ones >= zeros:
                mask = np.logical_not(mask).astype(int)

        new_codes = new_codes[mask.astype(bool)]

    return new_codes


def list_to_bit_value(list):
    """Convert list to bit value."""""

    bit_string = ''.join([str(x) for x in list])
    value = int(bit_string, 2)

    return value


def solver(file_name, part=1):
    """Solver for problem"""

    text = load_input(file_name)
    value = 0
    codes = np.array([[int(c) for c in line] for line in text])

    if part == 1:
        n_bits = codes.shape[1]

        gamma_list = [get_bit(codes[:, i], gamma=True) for i in range(n_bits)]
        gamma_value = list_to_bit_value(gamma_list)

        epsilon_list = [get_bit(codes[:, i], gamma=False) for i in range(n_bits)]
        epsilon_value = list_to_bit_value(epsilon_list)

        value = gamma_value * epsilon_value

    elif part == 2:
        code_oxygen = get_oxygen_co2(codes, oxygen=True)[0]
        value_oxygen = list_to_bit_value(code_oxygen)

        code_co2 = get_oxygen_co2(codes, oxygen=False)[0]
        value_co2 = list_to_bit_value(code_co2)

        value = value_co2 * value_oxygen

    print(f'Result for Part {part}')
    print(f'   Loaded: {file_name}')
    print(f'   The resulting value is: {value}')


def run_solvers(part1_input, part2_input, part1_example='example.txt', part2_example='example.txt'):
    """Run solvers for first and second part, including examples."""

    # Part 1
    if part1_example:
        solver(part1_example, part=1)

    if part1_input:
        solver(part1_input, part=1)

    # Part 2
    if part2_example:
        solver(part2_example, part=2)

    if part2_input:
        solver(part2_input, part=2)


if __name__ == '__main__':
    print_header()

    run_solvers(part1_example='example.txt',
                part1_input='input.txt',
                part2_example='example.txt',
                part2_input='input.txt')
