from aoc import read_txt, remove_empty, print_result, results


def card_split(card):
    card = card.split(':')[1]
    win = card.split('|')[0].strip().split(' ')
    win = remove_empty(win)
    num = card.split('|')[1].strip().split(' ')
    num = remove_empty(num)

    return win, num


def card_points(card):
    win, num = card_split(card)
    points = 0
    first = True
    for n in num:
        if n != '' and n in win:
            if first:
                points = 1
                first = False
            else:
                points *= 2

    return points


def all_points(cards):
    total_points = 0
    for card in cards:
        points = card_points(card)
        total_points += points
    return total_points


def calculate_cards(path, second_part = False):
    cards = read_txt(path)
    points = all_points(cards)

    return points



import os

day = os.path.basename(__file__).split(".")[0]

results(calculate_cards, day)

