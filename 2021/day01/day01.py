import numpy as np


def load_input(input_file):
    """Read the input file and return a list"""

    with open(f'input/{input_file}', 'r') as file:
        text = file.read().strip().splitlines()

    return text


def count_increases(x, increasing=True):
    """Count the number of increasing numbers"""

    difference = x[1:] - x[:-1]

    increasing_count = 0
    if increasing:
        increasing_count = np.sum(difference > 0)
    else:
        increasing_count = np.sum(difference < 0)

    return increasing_count


def moving_average(x, window=3):
    """Calculate the moving average"""

    avg_x = np.array([np.mean(x[i:i + window]) for i in range(len(x) - window + 1)])

    return avg_x


def solver(file_name, part=1):
    """Solver for problem"""

    text = load_input(file_name)
    sonars = np.array([int(entry) for entry in text])

    count = 0
    if part == 1:
        count = count_increases(sonars)

    if part == 2:
        sonars_avg = moving_average(sonars)
        count = count_increases(sonars_avg)

    print(f'Result for Part {part}')
    print(f'   Loaded: {file}')
    print(f'   The resulting count is: {count}')


if __name__ == '__main__':
    # Part 1
    file = 'example.txt'
    solver(file, part=1)

    file = 'input.txt'
    solver(file, part=1)

    # Part 2
    file = 'example.txt'
    solver(file, part=2)

    file = 'input.txt'
    solver(file, part=2)
