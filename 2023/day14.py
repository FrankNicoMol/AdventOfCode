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


def flip_north(board):
    board_tilted = []
    for array in board.T:
        board_tilted.append(tilt_array(array))
    board_final = np.array(board_tilted).T

    return board_final


def flip_cycle(board):
    for i in range(4):
        board = flip_north(board)
        board = np.rot90(board, k=3)

    return board


def cal_load(board):
    h, w = board.shape
    val_array = np.flip((np.arange(1, h + 1) * np.ones((h, w))).T)

    total = np.sum((board == 'O') * val_array)
    total = int(total)
    return total


def get_value(text, second):
    board = to_array(text)

    if second:
        reps = 1000000000

        board_dict = {}

        for i in range(reps):
            board_final = flip_cycle(board)
            board_flat = ''.join(board.flatten())
            if board_flat in board_dict.keys():
                last_idx = board_dict[board_flat]
                break
            else:
                board_dict[board_flat] = i
                board = board_final
        cycle = i - last_idx

        remainder = (reps - i) % cycle
        for i in range(remainder):
            board_final = flip_cycle(board)
            board = board_final
        total = cal_load(board_final)
    else:
        board_final = flip_north(board)
        total = cal_load(board_final)

    return total


day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
