from aoc import results, read_txt, remove_empty
import os
import numpy as np


def replace(val_list, val, replacer):
    """Replace value in list"""
    for i in range(len(val_list)):
        if val_list[i] == val:
            val_list[i] = replacer
    return val_list


def first_digit(line, second):
    """Find first digit"""

    if not second:
        dig = [str(x) for x in range(1, 10)]
        idx = [line.find(dig[i]) for i in range(9)]

        idx = replace(idx, -1, np.inf)
        val = dig[np.argmin(idx)]
    else:
        dig = [str(x) for x in range(1, 10)]
        idx = [line.find(dig[i]) for i in range(9)]
        dig2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        idx2 = [line.find(dig2[i]) for i in range(9)]
        idx = replace(idx, -1, np.inf)
        idx2 = replace(idx2, -1, np.inf)
        if np.min(idx) < np.min(idx2):
            val = dig[np.argmin(idx)]
        else:
            val = dig[np.argmin(idx2)]

    return val


def last_digit(line, second):
    '''Find last digit'''

    if not second:
        dig = [str(x) for x in range(1, 10)]
        idx = [line.rfind(dig[i]) for i in range(9)]
        val = dig[np.argmax(idx)]
    else:
        dig = [str(x) for x in range(1, 10)]
        dig2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        idx = [line.rfind(dig[i]) for i in range(9)]
        idx2 = [line.rfind(dig2[i]) for i in range(9)]
        if np.max(idx) > np.max(idx2):
            val = dig[np.argmax(idx)]
        else:
            val = dig[np.argmax(idx2)]

    return val


def find_number(line, second):
    '''Find code number'''
    val = int(first_digit(line, second) + last_digit(line, second))
    return val


def calculate_code(path, second):
    """Calculate code by finding first and last digit"""
    text = read_txt(path)
    num = np.sum([find_number(line, second) for line in text])
    return num


day = os.path.basename(__file__).split(".")[0]
results(calculate_code, day)
