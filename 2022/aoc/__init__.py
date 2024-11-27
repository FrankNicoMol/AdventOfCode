from pathlib import Path


def get_input_path(day):
    return f'input/day{day:02d}_input.txt'


def get_lines(day):
    """Get the lines for given input day."""

    path = get_input_path(day=day)
    lines = get_line_from_path(path)
    return lines


def get_line_from_path(path):
    """Get example of given path."""

    with open(path) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def print_header(day, year=2022):
    """Print header of solutions."""

    print(f'\nResult of Advent of Code, year {year}, day {day}')
    print(f'Find description at https://adventofcode.com/{year}/day/{day}\n')


def get_example_paths(day):
    """Get all example"""

    input_path = Path('input')
    examples_list = [str(p) for p in input_path.glob(f'*{day:02d}_example*')]
    return examples_list


def print_solution(part, solution):
    print(f'{part:<10}: {solution}')


def run_examples(day, f):
    """Run all examples for a given day."""

    example_paths = get_example_paths(day)
    for example_path in example_paths:
        lines = get_line_from_path(example_path)
        example_solution = f(lines)
        example_name = example_path.split('.')[0].split('_')[1]
        print_solution(part=example_name.capitalize(), solution=example_solution)
