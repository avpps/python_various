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

PATH = 'C://repositories//files//poker.txt'
figures_ordered = ['A', 'K', 'Q', 'J', 'T', '9', '8',
                   '7', '6', '5', '4', '3', '2']
figures = ''.join(figures_ordered)
colors = 'HDCS'

five_cards_set = [figures[i:i + 5] for i in range(len(figures) - 4)]


def c_ps(x):
    return r'(%s)' % '|'.join(x(n, i) for n, i in enumerate(five_cards_set))


def poker_krolewski():
    return r'(A([{c}])K\2Q\2J\2T\2)'

@c_ps
def poker(n, i):
    return ''.join('[%s]' % j + (
        '([%s])' % colors if m == 0 else '\%d' % (n + 2)
    ) for m, j in enumerate(i))


def kareta():
    return r'(([{f}])[{c}]\2[{c}]\2[{c}]\2[{c}])'


def kolor():
    return r'([{f}]([{c}])[{f}]\2[{f}]\2[{f}]\2[{f}]\2)'


@c_ps
def street(n, i):
    return ''.join(j + '[%s]' % colors for j in i)


def trio(x):
    return r'(([{f}])[{c}]\%d[{c}]\%d[{c}])' % (2 + x, 2 + x)


def couple(x):
    return r'(([{f}])[{c}]\%d[{c}])' % (2 + x)


def couple_couples():
    return r'((?<=[{f}][{c}])%s%s|%s[{f}][{c}]%s|%s%s(?=[{f}][{c}]))' % (
        couple(1), couple(3), couple(5), couple(7), couple(9), couple(11)
    )


def full():
    return r'(%s%s|%s%s)' % (
        couple(1), trio(3), trio(5), couple(7)
    )


schemes = [
    ('0_poker_krolewski', poker_krolewski()),
    ('1_poker', poker),
    ('2_kareta', kareta()),
    ('3_full', full()),
    ('4_kolor', kolor()),
    ('5_street', street),
    ('6_trojka', trio(0)),
    ('7_dwie_pary', couple_couples()),
    ('8_para', couple(0)),
    ('9_pusta', ''),
]
schemes_exp = [i[1].format(f=figures, c=colors) for i in schemes]


def sort_hand(hand):
    hand_sorted = sorted(hand, key=lambda x: figures_ordered.index(x[0]))
    return ''.join(hand_sorted)


def find_pattern(hand):
    hand_aggr = [None, None, None]
    for i, exp in enumerate(schemes_exp):
        figure = re.search(exp, hand)
        if figure:
            hand_aggr[0] = i
            if i == 7 and len(figure.group()) == 10:
                hand_aggr[1] = ''.join((figure.group(6), figure.group(8)))
            else:
                hand_aggr[1] = figure.group()
            break

    hand_aggr[2] = hand
    return hand_aggr


def compare(hand_1, hand_2, result):

    def check_all():
        for i, j in zip(hand_1[2][::2], hand_2[2][::2]):
            i_ord = figures_ordered.index(i)
            j_ord = figures_ordered.index(j)
            if i_ord < j_ord:
                result['gracz_1'] += 1
                break
            elif i_ord > j_ord:
                result['gracz_2'] += 1
                break

    h_1_0 = hand_1[0]
    h_2_0 = hand_2[0]
    if h_1_0 < h_2_0:
        result['gracz_1'] += 1
    elif h_1_0 > h_2_0:
        result['gracz_2'] += 1
    elif h_1_0 == h_2_0:
        if h_1_0 == 9:
            check_all()
        else:
            h_1_1_0_o = figures_ordered.index(hand_1[1][0])
            h_2_1_0_o = figures_ordered.index(hand_2[1][0])
            if h_1_1_0_o < h_2_1_0_o:
                result['gracz_1'] += 1
            elif h_1_1_0_o > h_2_1_0_o:
                result['gracz_2'] += 1
            else:
                check_all
    print(result, hand_1, hand_2)
    return result


result = {'gracz_1': 0, 'gracz_2': 0}

with open(PATH) as file:
    for line in file:
        hands = line.replace('\n', '').split(' ')
        hand_1 = find_pattern(sort_hand(hands[:5]))
        hand_2 = find_pattern(sort_hand(hands[5:]))
        result = compare(hand_1, hand_2, result)

print('\n\n', result)


def test_find_pattern():

    # poker_krolewski:
    assert find_pattern('AHKHQHJHTH')[0] == 0

    # poker:
    assert find_pattern('KHQHJHTH9H')[0] == 1

    # kareta:
    assert find_pattern('AHADACASJS')[0] == 2
    assert find_pattern('AHJDJCJSJH')[0] == 2

    # full:
    assert find_pattern('AHADAS2H2D')[0] == 3
    assert find_pattern('AHAD2S2H2D')[0] == 3

    # kolor:
    assert find_pattern('AHQHJHTH9H')[0] == 4

    # street:
    assert find_pattern('JHTD9C8S7H')[0] == 5

    # trojka:
    assert find_pattern('AHADAC2SJS')[0] == 6
    assert find_pattern('AHKDKCKHJS')[0] == 6
    assert find_pattern('AHKDQCQHQS')[0] == 6

    # dwie_pary:
    assert find_pattern('AHKHKD3H3D')[0] == 7
    assert find_pattern('AHADKDKC2S')[0] == 7
    assert find_pattern('AHADKSQDQC')[0] == 7

    # para:
    assert find_pattern('AHKDKDQC2S')[0] == 8
    assert find_pattern('AHKDJD3C3S')[0] == 8
    assert find_pattern('AHKDJD3C3S')[0] == 8

    # pusta:
    assert find_pattern('ASKHQHJH2H')[0] == 9


def test_compare():

    result = {'gracz_1': 0, 'gracz_2': 0}
    desired_resp = {'gracz_1': 1, 'gracz_2': 0}

    resp = compare(
        [3, 'AHADAS2H2D', 'AHADAS2H2D'],
        [4, 'AHQHJHTH9H', 'AHQHJHTH9H'],
        result.copy()
    )
    assert resp == desired_resp

    resp = compare(
        [9, '', 'ASKDJD8H3D'],
        [9, '', 'QD8C7C6C5C'],
        result.copy()
    )
    assert resp == desired_resp

    resp = compare(
        [3, 'AHADAS2H2D', 'AHADAS2H2D'],
        [3, 'KHKD2S2H2D', 'KHKD2S2H2D'],
        result.copy()
    )
    assert resp == desired_resp

    resp = compare(
        [8, 'AHKDJS2H2D', 'KHQD5S2H2D'],
        [8, 'KHKD2S2H2D', 'KHKD2S2H2D'],
        result.copy()
    )
    assert resp == desired_resp
