from aoc import get_lines, print_header, run_examples, print_solution
import os
import re
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


def get_solution(lines, part=1):
    """Generate the solution with given input lines."""

    # General applicability

    # Part I
    if not part - 1:
        nm = []
        for line in lines:
            muls = [line[m.start() + 4: m.start() + 12] for m in re.finditer('mul\(', line)]

            for m in muls:
                if ',' in m:
                    d1 = m.split(',')[0]
                    r = ('').join(m.split(',')[1:])
                    if r:
                        if r[:3].isdigit() and len(r) > 3:
                            if r[3] == ')':
                                nm.append([int(d1), int(r[:3])])
                        elif r[:2].isdigit() and len(r) > 2:
                            if r[2] == ')':
                                nm.append([int(d1), int(r[:2])])
                        elif r[0].isdigit() and len(r) > 1:
                            if r[1] == ')':
                                nm.append([int(d1), int(r[0])])
        solution = sum([a * b for a, b in nm])

    # Part II
    else:
        nm = []
        for line in lines:
            dos = [m.start() for m in re.finditer('do\(\)', line)]
            donts = [m.start() for m in re.finditer('don\'t\(\)', line)]
            dos.sort()
            donts.sort()
            muls = [m.start() for m in re.finditer('mul\(', line)]
            nmuls = []
            for m in muls:
                temp_dos = [d for d in dos if d < m]
                temp_donts = [d for d in donts if d < m]
                # print(temp_dos)
                # print(temp_donts)
                # print(m)
                if not temp_dos and not temp_donts:
                    nmuls.append(line[m + 4: m + 12])
                elif temp_dos and not temp_donts:
                    nmuls.append(line[m + 4: m + 12])
                elif temp_dos and temp_donts:
                    mdo = max(temp_dos)
                    mdont = max(temp_donts)
                    if mdont < mdo:
                        nmuls.append(line[m + 4: m + 12])

            for m in nmuls:
                if ',' in m:
                    d1 = m.split(',')[0]
                    r = ('').join(m.split(',')[1:])
                    if r:
                        if r[:3].isdigit() and len(r) > 3:
                            if r[3] == ')':
                                nm.append([int(d1), int(r[:3])])
                        elif r[:2].isdigit() and len(r) > 2:
                            if r[2] == ')':
                                nm.append([int(d1), int(r[:2])])
                        elif r[0].isdigit() and len(r) > 1:
                            if r[1] == ')':
                                nm.append([int(d1), int(r[0])])
            solution = sum([a * b for a, b in nm])

    return solution


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    solver(day)
