import numpy as np
import os
from scipy.signal import convolve2d


def get_day_number():
    """Obtain day number from filename."""

    filename = os.path.basename(__file__)
    no_extension = filename.split(".")[0]
    day_number = no_extension[-2:]
    day_integer = int(day_number)

    return day_integer


def print_header(year=2025):
    """Print header of solutions."""

    day = get_day_number()
    print(f'\nResult of Advent of Code, year {year}, day {day}')
    print(f'Find description at https://adventofcode.com/{year}/day/{day}\n')


def load_input(input_file):
    """Read the input file and return a list"""

    with open(f'input/{input_file}', 'r') as file:
        text = file.read().strip().splitlines()

    return text


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


def solve_part1(text):
    """Solve part 1."""

    array = convert_to_array(text)
    K = np.ones((3, 3), dtype=int)

    neighbours = convolve2d(array, K, mode="same", boundary="fill", fillvalue=0)
    low_num_neighbours = neighbours < 5
    available_rolls = array * low_num_neighbours
    value = np.sum(available_rolls)
    return value


def solve_part2(text):
    """Solve part 2."""

    array = convert_to_array(text)
    K = np.ones((3, 3), dtype=int)
    available = True
    value = 0
    while available:

        neighbours = convolve2d(array, K, mode="same", boundary="fill", fillvalue=0)
        low_num_neighbours = neighbours < 5
        available_rolls = array * low_num_neighbours
        num_available = np.sum(available_rolls)
        if num_available == 0:
            available = False
        value += num_available
        array -= available_rolls

    return value


def convert_to_array(text):
    """Convert text to a numpy array."""

    array = np.array([[c == '@' for c in line] for line in text]).astype(int)

    return array


def solver(file_name, part=1):
    """Solver for problem"""

    text = load_input(file_name)
    value = 0
    if part == 1:
        value = solve_part1(text)

    if part == 2:
        value = solve_part2(text)

    print(f'Result for Part {part}')
    print(f'   Loaded: {file_name}')
    print(f'   The resulting value is: {value}')


if __name__ == '__main__':
    print_header()
    run_solvers(part1_example='example.txt',
                part1_input='input.txt',
                part2_example='example.txt',
                part2_input='input.txt')
