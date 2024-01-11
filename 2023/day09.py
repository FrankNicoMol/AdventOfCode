from aoc import results, read_txt, remove_empty
import os
import numpy as np

def diffs(x):
    d = x[1:] - x[:-1]
    return d

def get_val(line, second):
    if not second:
        v = line[-1]
        while np.sum(line) != 0:
            line = diffs(line)
            v += line[-1]
    else:
        v = [line[0]]
        while np.sum(line) != 0:
            line = diffs(line)
            v.append(line[0])

        v.reverse()
        t = v[0]
        for i in v[1:]:
            t = i - t

        v = t
    return v

def get_value(path, second):
    text = read_txt(path)
    total = 0
    for line in text:
        line = line.split(' ')
        line = np.array([int(x) for x in line])
        val = get_val(line, second)
        total += val
    return total

day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
