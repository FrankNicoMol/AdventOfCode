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


def get_values_direction(line):
    """Get the direction and the number by line"""

    direction = line[0]
    num = int(line[1:])

    return direction, num


def solve_part_1(text, dial):
    """Solve part 1, count number of times dial ends at value 0."""

    value = 0
    for line in text:
        direction, num = get_values_direction(line)

        if direction == 'L':
            num *= -1

        dial += num

        if dial < 0:
            dial = 100 - (-1 * dial) % 100

        if dial > 99:
            dial = dial % 100

        if dial == 0:
            value += 1

    return value


def solve_part_2(text, dial):
    """Solve part 2, count number of times dial passed value 0."""

    value = 0
    for line in text:
        direction, num = get_values_direction(line)

        if direction == 'L':
            num *= -1

            if dial == 0:
                value -= 1

            dial += num

            while dial < 0:
                dial += 100
                value += 1
            if dial == 0:
                value += 1

        else:
            dial += num

            while dial > 99:
                dial -= 100
                value += 1

    return value


def solver(file_name, part=1):
    """Solver for problem"""

    text = load_input(file_name)

    value = 0
    if part == 1:
        value = solve_part_1(text, dial=50)
    if part == 2:
        value = solve_part_2(text, dial=50)

    print(f'Result for Part {part}')
    print(f'   Loaded: {file_name}')
    print(f'   The resulting value is: {value}')


if __name__ == '__main__':
    print_header()

    run_solvers(part1_example='example.txt',
                part1_input='input.txt',
                part2_example='example.txt',
                part2_input='input.txt')
