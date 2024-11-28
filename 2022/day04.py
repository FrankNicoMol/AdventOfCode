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


def get_vals(ran):
    ran_begin, ran_end = ran.split('-')
    ran_begin = int(ran_begin)
    ran_end = int(ran_end)
    return ran_begin, ran_end


def check_if_in(s_in, s_out):
    covered = False

    sin_begin, sin_end = get_vals(s_in)
    sout_begin, sout_end = get_vals(s_out)

    if sin_begin >= sout_begin and sin_end <= sout_end:
        covered = True
    if sin_begin <= sout_begin and sin_end >= sout_end:
        covered = True

    return covered


def check_overlap(s_in, s_out):
    covered = False

    sin_begin, sin_end = get_vals(s_in)
    sout_begin, sout_end = get_vals(s_out)

    if sin_begin >= sout_begin and sin_begin <= sout_end:
        covered = True
    if sin_begin <= sout_begin and sin_end >= sout_begin:
        covered = True

    return covered


def get_solution(lines, part=1):
    """Generate the solution with given input lines."""

    # General applicability

    # Part I
    if not part - 1:
        solution = 0
        for line in lines:
            s1, s2 = line.split(',')
            line_in = check_if_in(s1, s2)
            solution += line_in


    # Part II
    else:
        solution = 0
        for line in lines:
            s1, s2 = line.split(',')
            line_in = check_overlap(s1, s2)
            solution += line_in

    return solution


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    solver(day)
