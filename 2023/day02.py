from aoc import results, read_txt, remove_empty
import os


def get_cube_val(game, col):
    ''''Obtain the maximum number of values for given color'''
    val = 0
    for sub in game.split(';'):
        sub1 = sub.split(' ')[1:]

        for i in range(len(sub1) // 2):
            cube = sub1[2 * i + 1].replace(',', '')
            if cube == col:
                cube_val = int(sub1[2 * i])
                if cube_val > val:
                    val = cube_val

    return val


def game_possibile(game, colors, vals):
    '''Check if game is possible with given colors and numbers'''
    for col, val in zip(colors, vals):
        if get_cube_val(game, col) > val:
            return False

    return True


def powers(game, colors):
    '''Check if game is possible with given colors and numbers'''
    power = 1
    for col in colors:
        power *= get_cube_val(game, col)

    return power


def color_code(text, colors, vals, second):
    '''Returns color code'''

    sum = 0
    for n, line in enumerate(text):
        game = line.split(':')[1]
        if not second:
            if game_possibile(game, colors, vals):
                sum += n + 1
        else:
            sum += powers(game, colors)

    return sum


def crack_code(path, second):
    '''Returns cracked code'''

    colors = ['red', 'green', 'blue']
    vals = [12, 13, 14]
    text = read_txt(path)
    result = color_code(text, colors, vals, second)

    return result


day = os.path.basename(__file__).split(".")[0]
results(crack_code, day)
