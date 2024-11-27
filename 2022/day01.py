from aoc import get_lines, print_header, run_examples, print_solution
import os
import sys
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
    if part -1:
        print('')


def solver(day):
    run_examples(day, lambda x: get_solution(x, part=1))

    # Load data
    lines = get_lines(day=day)

    # Part 1
    print_solutions(lines, part=1)

    # Part 2
    print_solutions(lines, part=2)


def get_solution(lines, part=1):
    # General applicability
    elves = [sum([int(g) for g in group]) for item, group in groupby(lines, key=bool) if item]
    elves.sort(reverse=True)

    # Part I & Part II
    max_calories = sum(elves[:3]) if part - 1 else elves[0]

    return max_calories


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    solver(day)
