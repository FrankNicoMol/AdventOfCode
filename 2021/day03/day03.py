import numpy as np


def load_input(input_file):
    """Read the input file and return a list"""

    with open(f'input/{input_file}', 'r') as file:
        text = file.read().strip().splitlines()

    return text


def convert_movement(command):
    """Convert the command to movement"""

    direction, amount = command.split(' ')
    amount = int(amount)
    movement = np.array([0, 0])
    if direction == 'forward':
        movement[0] += amount
    elif direction == 'up':
        movement[1] -= amount
    elif direction == 'down':
        movement[1] += amount

    return movement


def solver(file_name, part=1):
    """Solver for problem"""

    text = load_input(file_name)
    value = 0

    if part == 1:
        movements = np.array([convert_movement(command) for command in text])
        value = np.prod(np.sum(movements, axis=0))

    if part == 2:
        movements = np.array([convert_movement(command) for command in text])

        pos = np.array([0, 0])
        aim = 0
        for move in movements:
            if move[1]:
                aim += move[1]
            else:
                pos[0] += move[0]
                pos[1] += move[0] * aim

        value = np.prod(pos)

    print(f'Result for Part {part}')
    print(f'   Loaded: {file}')
    print(f'   The resulting value is: {value}')


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
