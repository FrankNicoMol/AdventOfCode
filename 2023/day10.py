from aoc import results, read_txt, remove_empty
import os
import numpy as np
import matplotlib.pyplot as plt

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
    p, pos = next_pos(maze, start_pos, get_step('down'))
    if p == '|' or p == 'F' or p == '7':
        return 'down'

    p, pos = next_pos(maze, start_pos, get_step('left'))
    if p == '-' or p == 'L' or p == 'F':
        return 'left'
    p, pos = next_pos(maze, start_pos, get_step('up'))
    if p == '|' or p == 'L' or p == 'J':
        return 'up'


def inside(maze, ins, pos, d, direction):


    if d == 'start':
        return ins
    else:
        if d == 'right':
            if direction == 'right':
                n = pos + get_step('down')
            else:
                n = pos + get_step('up')


        elif d == 'down':
            if direction == 'right':
                n = pos + get_step('left')
            else:
                n = pos + get_step('right')
        elif d == 'left':
            if direction == 'right':
                n = pos + get_step('up')
            else:
                n = pos + get_step('down')
        elif d == 'up':
            if direction == 'right':
                n = pos + get_step('right')
            else:
                n = pos + get_step('left')
        h, w = maze.shape

        if not (n[0] < 0 or n[0] >= h or n[1] < 0 or n[1] >= w):
            if not maze[n[0], n[1]]:
                ins[n[0], n[1]] = 1
        return ins


def next_dir(maze, pos, d):
    p, pos_next = next_pos(maze, pos, get_step(d))
    cor_dir = None
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

def fill(ins_d, maze):
    h,w = maze.shape
    c = np.where(ins_d)
    while len(c[0]) > 0 and len(c[1]) > 0:
        nmaze = np.zeros(maze.shape)
        for x, y in np.array(c).T:
            if x+1 < h:
                if not maze[x + 1,y]  and ins_d[x+1,y] == 0:
                    nmaze[x + 1,y] = 1
            if x - 1 >= 0:
                if not maze[x - 1,y]  and ins_d[x-1,y] == 0:
                    nmaze[x - 1,y] = 1
            if y + 1 < w:
                if not maze[x,y + 1]  and ins_d[x,y+1] == 0:
                    nmaze[x,y + 1] = 1
            if y - 1 >= 0:
                if not maze[x,y - 1] and ins_d[x,y-1] == 0:
                    nmaze[x,y - 1] = 1
        c = np.where(nmaze)
        ins_d += nmaze
    return ins_d


def get_value(file, second):
    text = read_txt(file)
    maze = np.array([[*l] for l in text])

    bin_maze = np.zeros(maze.shape)
    pos = np.array(np.where(maze == 'S'))
    bin_maze[pos[0], pos[1]] = 1
    d = start_dir(maze, pos)

    step = 0
    while d != 'start':
        pos, d = next_dir(maze, pos, d)
        bin_maze[pos[0], pos[1]] = 1
        step += 1

    if not second:
        return step//2
    else:
        pos = np.array(np.where(maze == 'S'))
        d = start_dir(maze, pos)
        ins_right = np.zeros(maze.shape)
        ins_left = np.zeros(maze.shape)
        step = 0
        while d != 'start':

            old_d = d


            pos, d = next_dir(maze, pos, d)

            ins_right = inside(bin_maze, ins_right, pos, d, 'right')
            ins_left = inside(bin_maze, ins_left, pos, d, 'left')
            ins_right = inside(bin_maze, ins_right, pos, old_d, 'right')
            ins_left = inside(bin_maze, ins_left, pos, old_d, 'left')

            step += 1

        if np.sum(ins_right[0, :]) or np.sum(ins_right[-1, :]) or np.sum(ins_right[:, 0]) or np.sum(ins_right[:, -1]):
            ins = ins_left
        else:
            ins = ins_right
        #print(bin_maze + 2*fill(ins, bin_maze))


        return int(np.sum(fill(ins, bin_maze)))

day = os.path.basename(__file__).split(".")[0]
results(get_value, day)
