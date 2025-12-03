import numpy as np
import os


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


def turn_on_batteries(text, num_banks):
    value = 0

    for line in text:
        digits = []
        current_code = line
        for i in range(num_banks - 1, 0, -1):
            current_digit, index = largest_digit(current_code[:-i])
            digits.append(current_digit)
            current_code = current_code[index + 1:]
        current_digit, index = largest_digit(current_code)
        digits.append(current_digit)

        jolt = int(''.join([str(digit) for digit in digits]))
        value += jolt

    return value


def solve_part1(text):
    """Solve part 1."""
    value = turn_on_batteries(text, 2)
    return value


def solve_part2(text):
    """Solve part 2."""

    value = turn_on_batteries(text, 12)
    return value


def largest_digit(code):
    """Find the largest digit in a code."""

    for i in range(9, -1, -1):
        try:
            pos = code.index(str(i))
            largest = i
        except ValueError:
            pos = -1
            largest = -1
        if pos > -1:
            break
    return largest, pos


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
