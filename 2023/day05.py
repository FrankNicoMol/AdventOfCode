import numpy as np
import time


class ProgressBar:
    '''
    Progress of a loop.

        Attributes:
            self.start_time (int): starting time
    '''

    def __init__(self, max_iterations, title=''):
        '''
        The constructor for the ProgressBar class.

            Parameters:
                None
        '''

        self.start_time = time.time()
        self.max_iterations = max_iterations
        self.title = title
        print(f'{self.title}[0/{self.max_iterations}]{"◻" * 10}(0%).', end='\r')

    def seconds_to_minutes(self, seconds):
        '''
        Divides seconds into minutes and seconds.

                Parameters:
                        seconds (int): number of seconds to divide.

                Returns:
                        minutes (int): number of minitues that the input had.
                        seconds (int): remainder of seconds.
        '''

        minutes = seconds // 60
        seconds = seconds % 60

        return minutes, seconds

    def display(self, iteration):
        '''
        Display the progress and the ETA for a loop.

            Parameters:
                iteration (int): current iteration of the loop.

            Returns:
                None
        '''

        time_taken = int(time.time() - self.start_time)
        time_left = int((time_taken / (iteration + 1) *
                         (self.max_iterations - (iteration + 1))))

        minutes_taken, seconds_taken = self.seconds_to_minutes(time_taken)
        minutes_left, seconds_left = self.seconds_to_minutes(time_left)

        progress = (iteration + 1) / (self.max_iterations)

        print(
            f'{self.title}[{iteration + 1}/{self.max_iterations}]{"◼" * int(progress * 10)}{"◻" * (10 - int(progress * 10))}({int(100 * (iteration + 1) / self.max_iterations)}%). ETA = {time.ctime(time.time() + time_left)}. Time taken / left = {minutes_taken:02d}:{seconds_taken:02d} / {minutes_left:02d}:{seconds_left:02d}.',
            end='\r')


def read_txt(path):
    with open(path) as f:
        lines = f.readlines()

    text = []
    for l in lines:
        text.append(l.strip())
    return text


def get_inputs(line):
    inputs = line.split(':')[1].strip().split(' ')
    for i in range(len(inputs)):
        inputs[i] = int(inputs[i])
    return inputs


def to_range(line):
    vals = line.split(' ')
    r = list(range(int(vals[1]), int(vals[1]) + int(vals[2])))
    val = int(vals[0])
    return r, val


def use_rules(inputs, lines):
    positions = [-1] * 100
    for line in lines:
        r, v = to_range(line)
        for i in range(len(r)):
            positions[r[i]] = v + i
    for i in range(len(positions)):
        if positions[i] == -1:
            for j in range(100):
                if j not in positions:
                    positions[i] = j
                    break
    outputs = []
    for i in inputs:
        outputs.append(positions[i])
    return outputs


def get_locations(path):
    text = read_txt(path)
    first = True
    f = False
    lines = []
    inputs = get_inputs(text[0])
    pr = ProgressBar(len(text))
    for i in range(1, len(text)):
        if text[i] == '':
            first = True
            if lines != []:
                return inputs, lines
                inputs = use_rules(inputs, lines)
        elif first:
            first = False
            lines = []
        else:
            lines.append(text[i])
        time.sleep(0.01)
        pr.display(i)
    if lines != []:
        inputs = use_rules(inputs, lines)
    return inputs


def use_rules(inputs, lines):
    positions = [-1] * 100
    for line in lines:
        r, v = to_range(line)
        for i in range(len(r)):
            positions[r[i]] = v + i
    for i in range(len(positions)):
        if positions[i] == -1:
            for j in range(100):
                if j not in positions:
                    positions[i] = j
                    break
    outputs = []
    for i in inputs:
        outputs.append(positions[i])
    return outputs


import math
digits = int(math.log10(n))+1

def length(inputs):
    max_dig = 0
    for n in inputs:
        digits = int(math.log10(n))+1
        if digits > max_dig:
            max_dig = digits
    return max_dig

def to_range(line):
    vals = line.split(' ')
    r = [int(vals[1]), int(vals[1])+int(vals[2])]
    val = int(vals[0])
    return r, val


def use_rules2(inputs, lines):
    pow = length(inputs)
    a = np.arange(1, 10 ** pow)
    print(a)
    for line in lines:
        r, v = to_range(line)

        a[r[0]:r[1]] += (v - r[0])
    print(a)

use_rules2(inputs, lines)





