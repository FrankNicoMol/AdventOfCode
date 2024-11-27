def get_input_path(day, year=2024):
    return f'input/day{day:02d}_input.txt'


def get_example_path(day, year=2024):
    return f'input/day{day:02d}_example.txt'


def get_input(day, year=2024, example=False):
    path = get_input_path(day=day)
    with open(path) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def print_header(day, year=2024):
    print(f'Result of Advent of Code, year {year}, day {day}')
    print(f'Find description at https://adventofcode.com/{year}/day/{day}\n')
