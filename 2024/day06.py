from aoc import get_lines, print_header, run_examples, print_solution
import os
import numpy as np


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


def next_pos(m, steps):
    last = False
    if '^' in m:
        y, x = np.where(m == '^')[0][0], np.where(m == '^')[1][0]
        line = m[:y, x][::-1]
        first = np.where(line == '#')[0]
        if first.size > 0:
            first = first[0]
        else:
            first = len(line)
            last = True
        new_m = m.copy()
        new_m[y, x] = '.'
        new_m[y - first, x] = '>'
        steps[y - first: y + 1, x] = 1
    elif 'v' in m:
        y, x = np.where(m == 'v')[0][0], np.where(m == 'v')[1][0]
        line = m[y + 1:, x]
        first = np.where(line == '#')[0]
        if first.size > 0:
            first = first[0]
        else:
            first = len(line)
            last = True
        new_m = m.copy()
        new_m[y, x] = '.'
        new_m[y + first, x] = '<'
        steps[y: y + first + 1, x] = 1
    elif '>' in m:
        y, x = np.where(m == '>')[0][0], np.where(m == '>')[1][0]
        line = m[y, x + 1:]
        first = np.where(line == '#')[0]

        if first.size > 0:
            first = first[0]
        else:
            first = len(line)
            last = True
        new_m = m.copy()
        new_m[y, x] = '.'
        new_m[y, x + first] = 'v'
        steps[y, x: x + first + 1] = 1
    elif '<' in m:
        y, x = np.where(m == '<')[0][0], np.where(m == '<')[1][0]
        line = m[y, :x][::-1]
        first = np.where(line == '#')[0]

        if first.size > 0:
            first = first[0]
        else:
            first = len(line)
            last = True
        new_m = m.copy()
        new_m[y, x] = '.'
        new_m[y, x - first] = '^'
        steps[y, x - first: x + 1] = 1

    return new_m, last, steps


def get_solution(lines, part=1):
    """Generate the solution with given input lines."""

    # General applicability

    # Part I
    if not part - 1:

        m = np.array([[c for c in line] for line in lines])
        steps = np.zeros(m.shape)
        end = False

        while not end:
            m, end, steps = next_pos(m, steps)

        steps = steps.astype(int)
        solution = np.sum(steps)

    # Part II
    else:
        solution = ''

    return solution


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    solver(day)
