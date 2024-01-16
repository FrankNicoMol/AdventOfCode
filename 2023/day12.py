from aoc import results, read_txt, remove_empty
import os
import numpy as np
import itertools
def get_sets(string):
    q = str(string).split('.')
    lens = [len(qi) for qi in q if len(qi) != 0]
    return lens

def binary_to_string(bin):
    key = ['.', '#']
    new = [key[int(i)] for i in bin]
    return ''.join(new)

def get_line_val(line, second):
    v, n = line.split(' ')
    n = np.asarray(n.split(',')).astype(int)
    if second:
        v = '?'.join([v] * 5)
    n = list(n) * 5 if second else list(n)
    qms = np.where(np.array([*v]) == '?')
    reps = len(qms[0])
    lst = list(itertools.product([0, 1], repeat=reps))
    array =  np.zeros(np.array([*v]).shape) + (np.array([*v]) == '#')
    total = 0
    for li in lst:
        array[qms] = np.array(li)
        set_c = get_sets(binary_to_string(array))
        if set_c == n:
            total += 1
    return total


def get_value(file, second):
    text = read_txt(file)
    val = sum([get_line_val(line, second) for line in text])
    return val


day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
