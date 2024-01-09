def read_txt(path):
    """read .txt file and strip"""

    with open(path) as file:
        lines = file.readlines()

    text = [line.strip() for line in lines]

    return text


def remove_empty(line):
    """removes empties"""

    new_line = [item for item in line if item != '']

    return new_line


def print_result(day, type, second, result):
    """Print result"""

    print(f'{day} - {type:8s} - Part {1 + second}: {result:15d}')


def print_header(day):
    """Print header"""

    day_int = int(day[-2:])
    print(f'Result of Advent of Code, year 2023, day {day_int}')
    print(f'Find description at https://adventofcode.com/2023/day/{day_int}\n')


def results(fun, day):
    """Calculate results for examples, inputs and both parts"""

    print_header(day)
    path = f'input/{day}_'

    for second_part in range(2):
        for j in range(2):
            if j:
                input = 'input'
            else:
                input = 'example'

            value = fun(f'{path}{input}.txt', second_part)
            print_result(day, input, second_part, value)
