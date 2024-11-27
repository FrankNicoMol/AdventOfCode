def get_input_path(day, year=2022):
    return f'input/day{day:02d}_input.txt'


def get_example_path(day, year=2022):
    return f'input/day{day:02d}_example.txt'


def get_lines(day, args, year=2022):
    if len(args) > 1:
        path = get_example_path(day=day)
    else:
        path = get_input_path(day=day)

    with open(path) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def print_header(day, year=2022):
    print(f'Result of Advent of Code, year {year}, day {day}')
    print(f'Find description at https://adventofcode.com/{year}/day/{day}\n')
