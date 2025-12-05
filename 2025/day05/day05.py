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

    split = text.index("")

    ranges = text[:split]
    items = text[split + 1:]
    value = 0
    for item in items:
        item_val = int(item)
        for range in ranges:
            start, end = range.split("-")
            start = int(start)
            end = int(end)

            if start <= item_val <= end:
                value += 1
                break

    return value


def solve_part2(text):
    """Solve part 2."""

    split = text.index("")

    ranges = text[:split]

    ranges = [[int(r.split("-")[0]), int(r.split("-")[1])] for r in ranges]

    ranges.sort()

    updated_ranges = []
    i = 0
    value = 0
    while i < len(ranges):
        start, end = ranges[i]

        if not (updated_ranges == [] or i == len(ranges) - 1):
            for j in range(i + 1, len(ranges)):
                ts, te = ranges[j]
                if end + 1 >= ts:
                    if end < te:
                        end = te
                    i += 1
                else:
                    break
        value += end + 1 - start
        i += 1

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
