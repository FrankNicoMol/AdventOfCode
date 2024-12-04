from aoc import get_lines, print_header, run_examples, print_solution
import os
import numpy as np
import re


def get_day_number():
    """Obtain day number from filename."""

    filename = os.path.basename(__file__)
    no_extension = filename.split(".")[0]
    day_number = no_extension[-2:]
    day_integer = int(day_number)

    return day_integer


def print_solutions(lines, part=1):
    """Generate results and print solutions."""

    name = 'Part II' if part - 1 else 'Part I'
    print_solution(part=name, solution=get_solution(lines, part=part))
    if part - 1:
        print('')


def solver(day):
    """Generate the solutions for all data for given day."""

    # Load data
    lines = get_lines(day=day)

    # Part 1
    run_examples(day, lambda x: get_solution(x, part=1))
    print_solutions(lines, part=1)

    # Part 2
    run_examples(day, lambda x: get_solution(x, part=2))
    print_solutions(lines, part=2)


def get_occurences(lines):
    occ = sum([len(list(re.finditer('XMAS', line))) + len(list(re.finditer('XMAS', line[::-1]))) for line in lines])
    return occ


def get_solution(lines, part=1):
    """Generate the solution with given input lines."""

    # General applicability

    # Part I
    if not part - 1:
        m = np.array([list(line) for line in lines])

        h = [''.join(line) for line in m]
        v = [''.join(line) for line in m.T]

        diagonals = [m[::-1, :].diagonal(i) for i in range(-m.shape[0] + 1, m.shape[1])]
        d1 = [''.join(line) for line in diagonals]

        diagonals = [m.diagonal(i) for i in range(-m.shape[0] + 1, m.shape[1])]
        d2 = [''.join(line) for line in diagonals]

        solution = get_occurences(h)
        solution += get_occurences(v)
        solution += get_occurences(d1)
        solution += get_occurences(d2)

    # Part II
    else:
        m = np.array([list(line) for line in lines])
        h, w = m.shape
        alist = np.argwhere(m == 'A')

        solution = 0
        for x, y in alist:
            if 0 < x < w - 1 and 0 < y < h - 1:
                q = m[x - 1, y - 1] + m[x + 1, y - 1] + m[x - 1, y + 1] + m[x + 1, y + 1]
                if q.count('M') == 2 and q.count('S') == 2 and m[x - 1, y - 1] != m[x+1, y+1]:
                    solution += 1

    return solution


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    solver(day)
