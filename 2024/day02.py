from aoc import get_input, print_header
import os


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
    text = get_input(day=day)
