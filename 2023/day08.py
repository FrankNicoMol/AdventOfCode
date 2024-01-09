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

    if not second:
        dest_map = 'AAA'
        steps = 0
        while dest_map != 'ZZZ':
            dest_map = maps[dest_map][(dirs[steps % len(dirs)] == 'R')]
            steps += 1
        return steps
    else:
        dest_keys = []
        for k in maps.keys():
            if k[-1] == 'A':
                dest_keys.append(k)
        dest_keys = dest_keys
        num_keys = len(dest_keys)
        finished_keys = 0
        steps = 0
        while finished_keys != num_keys:
            new_dest_keys = []
            finished_keys = 0
            for k in dest_keys:
                key = maps[k][(dirs[steps % len(dirs)] == 'R')]
                new_dest_keys.append(key)

                if key[-1] == 'Z':
                    finished_keys += 1

            dest_keys = new_dest_keys
            steps += 1
            if steps % 10_000_000 == 0:
                print(steps)

        return steps


day = os.path.basename(__file__).split(".")[0]
results(calculate_steps, day)
