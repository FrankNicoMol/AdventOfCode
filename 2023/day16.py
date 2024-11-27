from aoc import results
import os
import numpy as np
import sys

sys.setrecursionlimit(4000)

dir_to_step = {'right': np.array([0, 1]),
               'left': np.array([0, -1]),
               'up': np.array([-1, 0]),
               'down': np.array([1, 0]),
               }
next_dir = {'right': {'.': ['right'],
                      '|': ['up', 'down'],
                      '-': ['right'],
                      '/': ['up'],
                      '\\': ['down'],
                      },
            'left': {'.': ['left'],
                     '|': ['up', 'down'],
                     '-': ['left'],
                     '/': ['down'],
                     '\\': ['up'],
                     },
            'down': {'.': ['down'],
                     '|': ['down'],
                     '-': ['left', 'right'],
                     '/': ['left'],
                     '\\': ['right'],
                     },
            'up': {'.': ['up'],
                   '|': ['up'],
                   '-': ['left', 'right'],
                   '/': ['right'],
                   '\\': ['left'],
                   },
            }
def to_array(m):
    mlist = []
    for mi in m:
        mlist.append([*mi])

    return np.asarray(mlist)

def next_pos(board, pos, step):
    h, w = board.shape
    new_pos = pos + step
    if new_pos[0] < 0 or new_pos[0] >= h or new_pos[1] < 0 or new_pos[1] >= w:
        return None, None

    return board[new_pos[0], new_pos[1]], new_pos
def update_energized(energized, pos):
    x,y = pos
    energized[x,y] = 1
    return energized
def get_key(pos, direction):
    key = f'{pos[0]},{pos[1]},{direction}'
    return key

def get_other_key(pos, direction):
    if direction == 'right':
        d = 'left'
    if direction == 'left':
        d = 'right'
    if direction == 'up':
        d = 'down'
    if direction == 'down':
        d = 'up'

    key = f'{pos[0]},{pos[1]},{direction}'
    return key
def next_step(board, pos, direction, energized, tdict):
    key = get_key(pos, direction)
    h,w = board.shape

    if key in tdict or get_other_key(pos, direction) in tdict:
        return energized, tdict
    else:
        tdict.append(key)
        p = board[pos[0], pos[1]]
        dirs = next_dir[direction][p]
        for d in dirs:
            step = dir_to_step[d]
            next_pos = pos + step
            if 0 <= next_pos[0] < h and next_pos[1] >= 0 and next_pos[1] < w:
                energized = update_energized(energized, next_pos)
                energized, tdict = next_step(board, next_pos, d, energized, tdict)

    return energized, tdict

def get_value(file, second):
    board = to_array(file)
    if not second:
        pos = np.array([0, 0])
        p = board[pos[0], pos[1]]
        direction = 'right'
        energized = np.zeros(board.shape)
        energized = update_energized(energized, pos)
        tdict = []

        energized, tdict = next_step(board, pos, direction, energized, tdict)
        val = int(np.sum(energized))

    else:
        h,w = board.shape
        inits = [[0, i, 'down'] for i in range(h)] + [[i, 0, 'right'] for i in range(w)] + [[w - 1, i, 'up'] for i in
                                                                                            range(h)] + [
                    [i, h - 1, 'left'] for i in range(w)]
        max_e = 0
        for i, init in enumerate(inits):
            if i % 20 == 0:
                print(f'Calculating: {i} / {len(inits) - 1}')
            pos = np.array([init[0], init[1]])
            direction = init[2]
            energized = np.zeros(board.shape)
            energized = update_energized(energized, pos)
            tdict = []

            energized, tdict = next_step(board, pos, direction, energized, tdict)

            max_e = np.max([int(np.sum(energized)), max_e])
        val = max_e
    return val



day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
