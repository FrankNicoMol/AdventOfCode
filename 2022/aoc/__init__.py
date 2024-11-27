from pathlib import Path


def get_input_path(day, year=2022):
    return f'input/day{day:02d}_input.txt'


def get_lines(day, year=2022):
    path = get_input_path(day=day)

    with open(path) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def get_example_lines(path):
    with open(path) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def print_header(day, year=2022):
    print(f'\nResult of Advent of Code, year {year}, day {day}')
    print(f'Find description at https://adventofcode.com/{year}/day/{day}\n')


def get_example_paths(day, year=2022):
    input_path = Path('input')
    examples_list = [str(p) for p in input_path.glob(f'*{day:02d}_example*')]
    return examples_list


def print_solution(part, solution):
    print(f'{part:<10}: {solution}')


def run_examples(day, f):
    example_paths = get_example_paths(day)
    for example_path in example_paths:
        lines = get_example_lines(example_path)
        example_solution = f(lines)
        example_name = example_path.split('.')[0].split('_')[1]
        print_solution(part=example_name.capitalize(), solution=example_solution)
