import numpy as np
import os
from aoc import results, read_txt, remove_empty


def get_ints(line, second):
    """convert line to ints"""

    line = remove_empty(line.split(' '))
    if second:
        line_int = int(''.join(line[1:]))
    else:
        line_int = [int(x) for x in line[1:]]

    return line_int


def get_vals(path, second):
    """obtain time and distance"""

    text = read_txt(path)

    time = get_ints(text[0], second)
    distance = get_ints(text[1], second)

    return time, distance


def race_code(path, second=False):
    """read .txt file and strip"""

    time, distance = get_vals(path, second)
    if second:
        value = sum([i*(time-i) > distance for i in range(time)])
    else:
        value = 1
        for t, d in zip(time, distance):
            value *= sum([i * (t - i) > d for i in range(t)])

    return value


day = os.path.basename(__file__).split(".")[0]
results(race_code, day)
