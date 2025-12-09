import numpy as np
import os
from scipy.signal import convolve2d
import datetime


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

    value = 0

    mat = np.array([[int(val) for val in line.split()] for line in text[:-1]])
    ops = [val for val in text[-1].split()]
    for i in range(len(ops)):
        line = mat[:, i]
        if ops[i] == '+':
            value += line.sum()
        elif ops[i] == '*':
            value += line.prod()

    return value


def solve_part2(text):
    """Solve part 2."""
    value = 0

    sheet = np.array([[c  for c in line] for line in text[:-1]])
    ops = [val for val in text[-1].split()]

    op_number = 0
    op_vals = []
    for i in range(sheet.shape[1]):
        line = sheet[:, i]
        if len(set(line)) == 1 and str(line[0]) == " ":
            if ops[op_number] == '+':
                value += np.array(op_vals).sum()
            elif ops[op_number] == '*':
                value += np.array(op_vals).prod()

            op_vals = []
            op_number += 1

        else:
            op_vals.append(int("".join(line).replace(" ", "")))

    if ops[op_number] == '+':
        value += np.array(op_vals).sum()
    elif ops[op_number] == '*':
        value += np.array(op_vals).prod()

    return value


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
