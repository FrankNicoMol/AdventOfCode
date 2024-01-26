from aoc import results
import os
import numpy as np


def split_list_by_entry(total_list, entry):
    """Split maps """

    split_list = []
    cur_list = []

    for line in total_list:
        if line == entry:
            split_list.append(cur_list.copy())
            cur_list = []
        else:
            cur_list.append(line)
    split_list.append(cur_list)

    return split_list


def to_array(list_of_strings):
    """List of strings to array of chars"""

    array_of_chars = np.asarray([[*c] for c in list_of_strings])

    return array_of_chars


def check_for_mirror(ti_map):
    """Check for mirror, return the index"""

    idx = 0
    h, w = ti_map.shape
    for i in range(1, w - 1):

        if i == 1 and np.array_equal(ti_map[:, 0], ti_map[:, 1]):
            idx = i
        elif i == np.array_equal(ti_map[:, w - 2], ti_map[:, w - 1]):
            idx = w - 1
        else:
            left = np.flip(ti_map[:, :i], axis=1)
            right = ti_map[:, i:]

            hl, wl = left.shape
            hr, wr = right.shape

            if wl > wr:
                m = wr
            else:
                m = wl

            if np.array_equal(left[:, :m], right[:, :m]):
                idx = i

    return idx

def check_smudge(ti_map):
    h, w = ti_map.shape

    val = 0
    for i in range(h):
        for j in range(w):
            q_map = ti_map.copy()
            if q_map[i, j] == '.':
                q_map[i, j] = '#'
            else:
                q_map[i, j] = '.'

            p = check_for_mirror(q_map)
            if p > val:
                val = p

            p = check_for_mirror(np.rot90(q_map)) * 100
            if p > val:
                val = p


    return val

def get_value(text, second):
    maps = split_list_by_entry(text, '')

    total = 0
    for m in maps:
        ti_map = to_array(m)
        if not second:
            val = check_for_mirror(np.rot90(ti_map)) * 100
            val += check_for_mirror(ti_map)
            total += val
        else:
            total += check_smudge(ti_map)


    return total


day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
