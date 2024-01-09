from aoc import results, read_txt, remove_empty
import os
import numpy as np


def app_left(line, c):
    """check the number on the left"""
    pnum = ''
    k = c - 1
    while k > -1:
        if line[k].isdigit():
            pnum = line[k] + pnum
            k -= 1
        else:
            k = -1
    return pnum


def app_right(line, c):
    """check the number on the right"""
    q = ''
    k = c + 1
    while k < len(line):
        if line[k].isdigit():
            q += line[k]
            k += 1
        else:
            k = len(line)
    return q


def gears(text):
    locs = np.where(np.array(text) == '*')
    sum = 0
    for i, j in zip(locs[0], locs[1]):
        sum += calculate_gear(text, i, j)
    return sum


def adjecents(text):
    sum = 0

    for i in range(len(text)):
        line = text[i]
        num = ''
        special = False
        for j in range(len(line)):
            char = line[j]
            if char.isdigit():
                num += char
                subtext = text[np.max([i - 1, 0]):np.min([len(text), i + 2])]
                if j == len(line) - 1:
                    calc = True
                else:
                    calc = False
                for k in range(len(subtext)):
                    subsub = subtext[k][np.max([j - 1, 0]):np.min([j + 2, len(line)])]
                    for c in subsub:
                        if c not in '1234567890.':
                            special = True
            else:
                calc = True
            if calc:
                if num != '' and special:
                    # print('yes', num)
                    sum += int(num)
                    special = False
                    num = ''
                elif num != '':
                    # print('not', num)
                    num = ''

    return sum


def adjecent_gears(path, second):
    text = read_txt(path)
    for i in range(len(text)):
        text[i] = list(text[i])
    if not second:
        result = adjecents(text)
    else:
        result = gears(text)

    return result


def calculate_gear(text, i, j):
    rows = list(range(max([0, i - 1]), min([len(text), i + 2])))
    cols = list(range(max([0, j - 1]), min([len(text[0]), j + 2])))
    tnums = []
    count = 0
    for r in rows:
        num = ''
        line = text[r]
        double = False
        if line[cols[0]].isdigit():
            num = app_left(line, cols[0]) + line[cols[0]]
        if len(cols) == 2:
            if line[cols[1]].isdigit():
                num += line[cols[1]] + app_right(line, cols[1])
        else:
            if line[cols[1]].isdigit():
                num += line[cols[1]]
                if line[cols[2]].isdigit():
                    num += line[cols[2]] + app_right(line, cols[2])
            elif line[cols[2]].isdigit():
                if num != '':
                    num = [num, line[cols[2]] + app_right(line, cols[2])]
                    double = True
                else:
                    num += line[cols[2]] + app_right(line, cols[2])
        if num != '':
            if double:
                tnums.append(num[0])
                tnums.append(num[1])
                count += 2
            else:
                tnums.append(num)
                count += 1
    if count == 2:
        power = int(tnums[0]) * int(tnums[1])
    else:
        power = 0

    return power


day = os.path.basename(__file__).split(".")[0]
results(adjecent_gears, day)
