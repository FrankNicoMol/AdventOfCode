from aoc import results
import os
import scipy
import numpy as np

dir_to_step = {'R': np.array([0, 1]),
               'L': np.array([0, -1]),
               'U': np.array([-1, 0]),
               'D': np.array([1, 0]),
               '0': np.array([0, 1]),
               '1': np.array([0, -1]),
               '2': np.array([-1, 0]),
               '3': np.array([1, 0]),
               }

def next_pos(pos, d):

    new_pos = pos + dir_to_step[d]
    return new_pos
def get_value(file, second):
    all_pos = []
    pos = np.array([0, 0])
    all_pos.append(pos)
    max_x = 0
    max_y = 0


    for l in file:

        t, v, c = l.split(' ')
        if second:
            t = c[-2]
            v = int(c[2:-2], 16)


        for i in range(int(v)):

            pos = next_pos(pos, t)
            all_pos.append(pos)

    miny, minx = np.min(np.array(all_pos), axis=0)
    maxy, maxx = np.max(np.array(all_pos), axis=0)
    board = np.zeros((maxy - miny + 1, maxx - minx + 1)).astype(int)

    for pos in all_pos:
        board[pos[0] - miny, pos[1] - minx] = 1


    board = scipy.ndimage.binary_fill_holes(board)

    val = np.sum(board)

    return val



day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
