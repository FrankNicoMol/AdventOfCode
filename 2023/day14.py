from aoc import results
import os
import numpy as np


def to_array(m):
    mlist = []
    for mi in m:
        mlist.append([*mi])

    return np.asarray(mlist)


def tilt_array(array):
    array_string = ''.join(array)
    splitted = array_string.split('#')
    final_list = []
    for sub in splitted:
        sub_list = [*sub]
        sub_list.sort(reverse=True)
        final_list.append(''.join(sub_list))
    final_string = '#'.join(final_list)
    final_array = np.array([*final_string])
    return final_array


def get_value(text, second):
    board = to_array(text)

    board_tilted = []
    for array in board.T:
        board_tilted.append(tilt_array(array))
    board_final = np.array(board_tilted).T

    h, w = board_final.shape
    val_array = np.flip((np.arange(1, h + 1) * np.ones((h, w))).T)

    total = np.sum((board_final == 'O') * val_array)
    total = int(total)

    return total


day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
