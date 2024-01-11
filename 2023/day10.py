from aoc import results, read_txt, remove_empty
import os
import numpy as np

def get_step(direction):

    if direction == 'right':
        step = np.array([0,1]).reshape((2,1))
    elif direction == 'left':
        step= np.array([0,-1]).reshape((2,1))
    elif direction == 'up':
        step=np.array([-1,0]).reshape((2,1))
    elif direction == 'down':
        step= np.array([1,0]).reshape((2,1))
    return step

def next_pos(maze, pos, step):
    h, w = maze.shape
    new_pos = pos + step
    if new_pos[0] < 0 or new_pos[0] >= h or new_pos[1] < 0 or new_pos[1] >= w:
        return None, None

    return maze[new_pos[0], new_pos[1]], new_pos


def start_dir(maze, start_pos):
    p, pos = next_pos(maze, start_pos, get_step('right'))
    if p == '-' or p == 'J' or p == '7':
        return 'right'
    p, pos = next_pos(maze, start_pos, get_step('left'))
    if p == '-' or p == 'L' or p == 'F':
        return 'left'
    p, pos = next_pos(maze, start_pos, get_step('up'))
    if p == '|' or p == 'L' or p == 'J':
        return 'up'
    p, pos = next_pos(maze, start_pos, get_step('down'))
    if p == '|' or p == 'F' or p == '7':
        return 'down'


def next_dir(maze, pos, d):
    p, pos_next = next_pos(maze, pos, get_step(d))
    if d == 'right':
        if p == 'S':
            next_d = 'start'
        elif p == '-':
            next_d = 'right'
        elif p == 'J':
            next_d = 'up'
        elif p == '7':
            next_d = 'down'
    if d == 'left':
        if p == 'S':
            next_d = 'start'
        elif p == '-':
            next_d = 'left'
        elif p == 'F':
            next_d = 'down'
        elif p == 'L':
            next_d = 'up'
    if d == 'up':
        if p == 'S':
            next_d = 'start'
        elif p == '|':
            next_d = 'up'
        elif p == '7':
            next_d = 'left'
        elif p == 'F':
            next_d = 'right'
    if d == 'down':
        if p == 'S':
            next_d = 'start'
        elif p == '|':
            next_d = 'down'
        elif p == 'J':
            next_d = 'left'
        elif p == 'L':
            next_d = 'right'
    return pos_next, next_d
def get_value(file, second):
    text = read_txt(file)
    maze = np.array([[*l] for l in text])


    pos = np.array(np.where(maze == 'S'))
    d = start_dir(maze, pos)
    step = 0
    while d != 'start':
        pos, d = next_dir(maze, pos, d)

        step +=1
    return step//2

day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
