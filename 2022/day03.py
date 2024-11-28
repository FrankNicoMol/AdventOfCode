from aoc import get_lines, print_header, run_examples, print_solution
import os
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

    run_examples(day, lambda x: get_solution(x, part=1))

    # Load data
    lines = get_lines(day=day)

    # Part 1
    print_solutions(lines, part=1)

    run_examples(day, lambda x: get_solution(x, part=2))

    # Part 2
    print_solutions(lines, part=2)


def duplicates(line):
    line_length = len(line)
    l1 = line[:line_length // 2]
    l2 = line[line_length // 2:]

    dup = list(set([c1 for c1 in l1 if c1 in l2]))

    return dup


def get_priority(items):
    priority_val = 0
    for item in items:
        if item.isupper():
            priority_val += ord(item) - 38
        else:
            priority_val += ord(item) - 96
    return priority_val


def same_in_set(line_set):
    l1, l2, l3 = line_set

    dup = list(set([c1 for c1 in l1 if c1 in l2 and c1 in l3]))

    return dup


def get_solution(lines, part=1):
    """Generate the solution with given input lines."""

    # General applicability

    # Part I
    if not part - 1:
        solution = 0
        for line in lines:
            dup = duplicates(line)
            solution += get_priority(dup)

    # Part II
    else:
        solution = 0
        for line_set in zip(lines[::3], lines[1::3], lines[2::3]):
            dup = same_in_set(line_set)
            solution += get_priority(dup)

    return solution


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    solver(day)
