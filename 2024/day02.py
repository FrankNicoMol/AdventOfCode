from aoc import get_lines, print_header, run_examples, print_solution
import os
import numpy as np
from itertools import groupby


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


def get_solution(lines, part=1):
    """Generate the solution with given input lines."""

    # General applicability

    # Part I
    if not part - 1:
        solution = 0
        for line in lines:
            levels = np.array([int(val) for val in line.split(' ')])
            difference = levels[1:] - levels[:-1]
            if len(np.unique(np.sign(difference))) == 1:
                abs_diff = np.absolute(difference)
                jump = (0 < abs_diff) * (abs_diff <= 3)
                solution += np.all(jump)

    # Part II
    else:
        solution = 0
        for line in lines:
                levels = np.array([int(val) for val in line.split(' ')])

                for i in range(len(levels)):
                    nlevels = np.delete(levels, i)

                    difference = nlevels[1:] - nlevels[:-1]
                    if len(np.unique(np.sign(difference))) == 1:
                        abs_diff = np.absolute(difference)
                        jump = (0 < abs_diff) * (abs_diff <= 3)
                        if np.all(jump):
                            solution += 1
                            break



    return solution


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    solver(day)
