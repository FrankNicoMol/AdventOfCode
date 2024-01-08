import numpy as np



def hand_combo(cards, joker):

    sets = [cards.count(card) for card in set(cards)]
    if 'J' in cards and joker:
        val = cards.count('J')
        sets[sets.index(val)] = 0
        sets.sort(reverse = True)
        sets[0] += val
    else:
        sets.sort(reverse=True)
    sets += [0]*(len(cards) - len(sets))

    return sets

def first_wins(hand1, hand2, combo1, combo2, joker):

    if joker:
        pow = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    else:
        pow = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    for c1, c2 in zip(combo1, combo2):
        if c1 == c2:
            continue
        elif c1 > c2:
            return True
        else:
            return False

    for h1, h2 in zip(hand1, hand2):
        i1 = pow.index(h1)
        i2 = pow.index(h2)
        if i1 == i2:
            continue
        elif i1 < i2:
            return True
        else:
            return False

def calculate_win_money(path, joker = False):
    text = read_txt(path)

    hands = [line.split(' ') for line in text]

    combos = [hand_combo(hand[0], joker) for hand in hands]

    total_amount = 0

    for i in range(len(combos)):
        wins = 0
        for j in range(len(combos)):
            if i != j:
                wins += first_wins(hands[i][0], hands[j][0], combos[i], combos[j], joker)

        total_amount += np.compat.long((wins+1) * int(hands[i][1]))

    print(f'The resulting answer for {path} = {total_amount}  (joker: {joker} -- Part {1 + joker})')


calculate_win_money('example.txt')
calculate_win_money('input.txt')
calculate_win_money('example.txt', joker = True)
calculate_win_money('input.txt', joker = True)