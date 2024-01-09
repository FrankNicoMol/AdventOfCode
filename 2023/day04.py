from aoc import read_txt, remove_empty, print_result, results
import os
import numpy as np


def card_split(card):
    """Split the string in corresponding values"""

    card = card.split(':')[1]
    win = card.split('|')[0].strip().split(' ')
    win = remove_empty(win)
    num = card.split('|')[1].strip().split(' ')
    num = remove_empty(num)

    return win, num


def card_points(card, second=False):
    """Calculate the points of card"""

    win, num = card_split(card)
    points = 0

    if second:
        for n in num:
            if n != '' and n in win:
                points += 1
    else:
        first = True
        for n in num:
            if n != '' and n in win:
                if first:
                    points = 1
                    first = False
                else:
                    points *= 2

    return points


def all_points(cards, second=False):
    """Calculate all points"""

    total_points = [card_points(card, second) for card in cards]
    if not second:
        total_points = np.sum(total_points)

    return total_points


def calculate_cards(path, second=False):
    """Load and calculate"""

    cards = read_txt(path)
    points = all_points(cards, second)

    if second:
        points = np.array(points)

        mult = np.ones(points.shape)
        for i in range(len(points)):
            l = np.min([points[i], len(points) - i])
            add = np.ones(l) * mult[i]
            mult[i + 1:i + l + 1] += add
        points = int(np.sum(mult))

    return points


day = os.path.basename(__file__).split(".")[0]

results(calculate_cards, day)
