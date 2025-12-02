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


def solve_part1(id_ranges):
    """Solve part 1."""

    invalid_ids = []
    for id_range in id_ranges:
        start, end = id_range.split('-')
        start = int(start)
        end = int(end)

        for i in range(start, end + 1):
            code = str(i)
            len_code = len(code)
            half = len_code // 2
            # print(i, len_code, code[:half], code[half:], code[:half] == code[half:])
            if code[:half] == code[half:]:
                invalid_ids.append(int(code))

    value = sum(invalid_ids)
    return value


def chunks(code_list, k):
    """Yield successive n-sized chunks from l."""

    chunks_list = [code_list[i:i + k] for i in range(0, len(code_list), k)]

    return chunks_list


def solve_part2(id_ranges):
    """Solve part 1."""

    invalid_ids = []
    for id_range in id_ranges:
        start, end = id_range.split('-')
        start = int(start)
        end = int(end)

        for i in range(start, end + 1):
            code = str(i)
            len_code = len(code)

            for j in range(1, len_code // 2 + 1):
                code_chunks = chunks(code, j)
                if len(set(code_chunks)) == 1:
                    invalid_ids.append(int(code))
                    break

    value = sum(invalid_ids)

    return value


def solver(file_name, part=1):
    """Solver for problem"""

    text = load_input(file_name)[0]
    id_ranges = text.split(',')
    value = 0
    if part == 1:
        value = solve_part1(id_ranges)

    if part == 2:
        value = solve_part2(id_ranges)

    print(f'Result for Part {part}')
    print(f'   Loaded: {file_name}')
    print(f'   The resulting value is: {value}')


if __name__ == '__main__':
    print_header()

    run_solvers(part1_example='example.txt',
                part1_input='input.txt',
                part2_example='example.txt',
                part2_input='input.txt')
