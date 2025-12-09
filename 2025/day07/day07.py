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
    mat = np.array([[c for c in line] for line in text])
    for i in range(len(mat) - 2):
        block = mat[i:i + 3]
        sindex = np.where(block[0] == "S")[0]
        if len(sindex) > 0:
            mat[i + 1, sindex[0]] = "|"

        split_index = np.where(block[1] == "^")[0]
        if len(split_index) > 0:

            for ind in split_index:
                if mat[i, ind] == "|":
                    value += 1
                    if ind - 1 > -1:
                        mat[i + 1, ind - 1] = "|"
                    if ind + 1 < len(mat):
                        mat[i + 1, ind + 1] = "|"

        split_index = np.where(block[1] == "|")[0]
        if len(split_index) > 0:
            for ind in split_index:

                if mat[i + 2, ind] == ".":
                    mat[i + 2, ind] = "|"

    return value


def solve_part2(text):
    """Solve part 2."""
    value = 0
    mat = np.array([[c for c in line] for line in text])
    vals_mat = np.zeros(mat.shape).astype(int)
    for i in range(len(mat) - 2):
        block = mat[i:i + 3]
        sindex = np.where(block[0] == "S")[0]
        if len(sindex) > 0:
            mat[i + 1, sindex[0]] = "|"

        split_index = np.where(block[1] == "^")[0]
        if len(split_index) > 0:

            for ind in split_index:
                if mat[i, ind] == "|":
                    if ind - 1 > -1:
                        mat[i + 1, ind - 1] = "|"
                    if ind + 1 < len(mat):
                        mat[i + 1, ind + 1] = "|"

        split_index = np.where(block[1] == "|")[0]
        if len(split_index) > 0:
            for ind in split_index:

                if mat[i + 2, ind] == ".":
                    mat[i + 2, ind] = "|"
    for i in range(len(mat)):
        line = len(mat) - i - 1
        if i == 0:
            # arr = np.array().astype(int)

            vals_mat[line] = [1 if c == '|' else 0 for c in mat[line]]

            # mat[line] = np.array([1 if c == '|' else c for c in mat[line]])
        elif i == len(mat) - 1:
            sindex = np.where(mat[line] == "S")[0]
            value = vals_mat[line + 1, sindex[0]]
        else:
            for j in range(len(mat[line])):
                if mat[line, j] == "|" and vals_mat[line + 1, j] > 0:
                    vals_mat[line, j] = vals_mat[line + 1, j]
            for j in range(len(mat[line])):
                if mat[line - 1, j] == "|" and mat[line, j] == "^":
                    cval = 0
                    if j - 1 > -1:
                        cval += vals_mat[line, j - 1]
                    if j + 1 < len(mat[line]):
                        cval += vals_mat[line, j + 1]
                    vals_mat[line - 1, j] = cval
        # print(vals_mat)
    print(vals_mat)

    return value


def solver(file_name, part=1):
    """Solver for problem"""

    text = load_input(file_name)
    value = 0
    if part == 1:  # and 'example.txt' in file_name:
        value = solve_part1(text)

    if part == 2:  # and 'example.txt' in file_name:
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
