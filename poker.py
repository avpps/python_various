""" Script for find result of poker game saved in
txt file with following structure:

    - each line is one game
    - each item is one card
    - first 5 items in line is player_1 hand
    - last 5 items in line is player_2 hand

8C TS KC 9H 4S 7D 2S 5D 3S AC
5C AD 5D AC 9C 7C 5H 8D TD KS
3H 7H 6S KC JS QH TD JC 2D 8S

"""

import re
import pdb

PATH = 'C://repositories//files//poker_1.txt'
FIGURES_ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
FIGURES = ''.join(FIGURES_ORDER)
COLORS = 'HDCS'

schemes = [
    ('poker_krolewski', r'A[{c}]K[{c}]Q[{c}]J[{c}]T[{c}]'),
    ('poker', ''),
    ('kareta', r'([{f}])[{c}]\1[{c}]\1[{c}]\1[{c}]'),
    ('full', ''),
    ('kolor', r'[{f}]([{c}])[{f}]\1[{f}]\1[{f}]\1[{f}]\1'),
    ('street', 'FaNaNaNaNa'),
    ('trojka', r'([{f}])[{c}]\1[{c}]\1[{c}]'),
    ('dwie_pary', r'(([{f}])[{c}]\1[{c}]){{2}}'),
    ('para', r'([{f}])[{c}]\1[{c}]'),
    ('pusta', ''),
]
schemes_exp = [i[1].format(f=FIGURES, c=COLORS) for i in schemes]


def sort_hand(hand):
    hand_sorted = sorted(hand, key=lambda x: FIGURES_ORDER.index(x[0]))
    return ''.join(hand_sorted)


def find_pattern(hand):
    hand_aggr = [None, None, None]
    for i, exp in enumerate(schemes_exp):
        if i == 7: pdb.set_trace()
        figure = re.search(exp, hand)
        if figure and figure[0]:
            print(figure)
            hand_aggr[0] = i
            hand_aggr[1] = figure[0]
            break
    hand_aggr[2] = hand

    print('\n', hand_aggr)

    return hand_aggr


def compare(player_1, player_2, result):
    result_updated = None
    return result_updated


# result = {'gracz_1': 0, 'gracz_2': 0}
#
# with open(PATH) as file:
#     for line in file:
#         hands = line.replace('\n', '').split(' ')
#         hand_1 = find_pattern(sort_hand(hands[:5]))
#         hand_2 = find_pattern(sort_hand(hands[5:]))
#         result = compare(hand_1, hand_2, result)
#
# print(result['gracz_1'])


def test_find_pattern():

    # assert find_pattern('AHKHQHJHTH')[0] == 0
    # assert find_pattern('AHKDQCJSTH')[0] == 0

    # assert find_pattern('') == 1
    #
    # assert find_pattern('AHADACASJS')[0] == 2
    # assert find_pattern('AHJDJCJSJH')[0] == 2
    #
    # assert find_pattern('') == 3
    #
    # assert find_pattern('AHQHJHTH9H')[0] == 4
    #
    # assert find_pattern('')[0] == 5
    #
    # assert find_pattern('AHADAC2SJS')[0] == 6
    # assert find_pattern('AHKDKCKHJS')[0] == 6
    # assert find_pattern('AHADQCQHQS')[0] == 6
    #
    assert find_pattern('AHADKH2H2D')[0] == 7
    #
    # assert find_pattern('AHADKDKC2S')[0] == 8
    # assert find_pattern('AHKDKDQC2S')[0] == 8
    # assert find_pattern('AHKDJD3C3S')[0] == 8
    # assert find_pattern('AHADJD3C3S')[0] == 8
    #
    # assert find_pattern('')[0] == 9

# re.search('(?:.*)([AKQJT98765432])[HDCS]\\1[HDCS](?:.*)([AKQJT98765432])[HDCS]\\2[HDCS](?:.*)', 'AHADKH2H2D')