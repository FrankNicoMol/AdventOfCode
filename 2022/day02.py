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

    # Examples part 2
    run_examples(day, lambda x: get_solution(x, part=2))

    # Part 2
    print_solutions(lines, part=2)


scores1 = {'A': {'X': 3 + 1,
                 'Y': 6 + 2,
                 'Z': 0 + 3},
           'B': {'X': 0 + 1,
                 'Y': 3 + 2,
                 'Z': 6 + 3},
           'C': {'X': 6 + 1,
                 'Y': 0 + 2,
                 'Z': 3 + 3}
           }

scores2 = {'A': {'X': 0 + 3,
                 'Y': 3 + 1,
                 'Z': 6 + 2},
           'B': {'X': 0 + 1,
                 'Y': 3 + 2,
                 'Z': 6 + 3},
           'C': {'X': 0 + 2,
                 'Y': 3 + 3,
                 'Z': 6 + 1}
           }


def get_solution(lines, part=1):
    """Generate the solution with given input lines."""

    # General applicability

    # Part I
    if not part - 1:
        all = []
        for line in lines:
            opp, me = line.split(' ')
            score = scores1[opp][me]
            all.append(score)

        solution = sum(all)

    # Part II
    else:
        all = []
        for line in lines:
            opp, me = line.split(' ')
            score = scores2[opp][me]
            all.append(score)
        solution = sum(all)

    return solution


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    solver(day)
