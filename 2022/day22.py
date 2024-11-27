from aoc import get_lines, print_header
import os
import sys


def get_day_number():
    """Obtain day number from filename."""

    filename = os.path.basename(__file__)
    no_extension = filename.split(".")[0]
    day_number = no_extension[-2:]
    day_integer = int(day_number)

    return day_integer


if __name__ == "__main__":
    day = get_day_number()
    print_header(day=day)
    lines = get_lines(day = day, args = sys.argv)
