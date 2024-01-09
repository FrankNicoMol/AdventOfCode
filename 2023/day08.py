from aoc import results, read_txt, remove_empty
import os


def read_map(file):
    text = read_txt(file)
    dirs = text[0]
    maps = text[2:]

    maps_list = {}
    for m in maps:
        map_split = m.split('=')
        maps_list[map_split[0].strip()] = [map_split[1].split(',')[0].strip()[1:],
                                           map_split[1].split(',')[1].strip()[:-1]]

    return dirs, maps_list


def calculate_steps(file, second):
    dirs, maps = read_map(file)
    dest_map = 'AAA'
    steps = 0
    while dest_map != 'ZZZ':
        dest_map = maps[dest_map][(dirs[steps % len(dirs)] == 'R')]
        steps += 1
    return steps


day = os.path.basename(__file__).split(".")[0]
results(calculate_steps, day)
