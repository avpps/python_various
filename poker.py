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
cards_rank = ['A', 'K', 'Q', 'J', 'T', '9', '8',
                   '7', '6', '5', '4', '3', '2']
cards = ''.join(cards_rank)
suits = 'HDCS'

five_cards_set = [cards[i:i + 5] for i in range(len(cards) - 4)]


def c_sf_s(x):
    return r'(%s)' % '|'.join(x(n, i) for n, i in enumerate(five_cards_set))


def royal_flush():
    return r'(A([{c}])K\2Q\2J\2T\2)'

@c_sf_s
def straight_flush(n, i):
    return ''.join('[%s]' % j + (
        '([%s])' % suits if m == 0 else '\%d' % (n + 2)
    ) for m, j in enumerate(i))


def quads():
    return r'(([{f}])[{c}]\2[{c}]\2[{c}]\2[{c}])'


def flush():
    return r'([{f}]([{c}])[{f}]\2[{f}]\2[{f}]\2[{f}]\2)'


@c_sf_s
def straight(n, i):
    return ''.join(j + '[%s]' % suits for j in i)


def three(x):
    return r'(([{f}])[{c}]\%d[{c}]\%d[{c}])' % (2 + x, 2 + x)


def pair(x):
    return r'(([{f}])[{c}]\%d[{c}])' % (2 + x)


def two_pair():
    return r'((?<=[{f}][{c}])%s%s|%s[{f}][{c}]%s|%s%s(?=[{f}][{c}]))' % (
        pair(1), pair(3), pair(5), pair(7), pair(9), pair(11)
    )


def full():
    return r'(%s%s|%s%s)' % (
        pair(1), three(3), three(5), pair(7)
    )


hand_ranking = [
    ('0_poker_krolewski', royal_flush()),
    ('1_poker', straight_flush),
    ('2_kareta', quads()),
    ('3_full', full()),
    ('4_kolor', flush()),
    ('5_street', straight),
    ('6_trojka', three(0)),
    ('7_dwie_pary', two_pair()),
    ('8_para', pair(0)),
    ('9_pusta', ''),
]
hand_ranking_reg = [i[1].format(f=cards, c=suits) for i in hand_ranking]


def sort_hand(hand):
    hand_sorted = sorted(hand, key=lambda x: cards_rank.index(x[0]))
    return ''.join(hand_sorted)


def find_hand(hand):
    hand_aggr = [None, None, None]
    for i, exp in enumerate(hand_ranking_reg):
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

    def check(v_1, v_2, v_e=False):
        if v_1 < v_2:
            result['gracz_1'] += 1
        elif v_1 > v_2:
            result['gracz_2'] += 1
        else:
            if v_e:
                v_e()

    def check_all():
        for i, j in zip(hand_1[2][::2], hand_2[2][::2]):
            i_ord = cards_rank.index(i)
            j_ord = cards_rank.index(j)
            if i_ord < j_ord:
                result['gracz_1'] += 1
                break
            elif i_ord > j_ord:
                result['gracz_2'] += 1
                break

    def check_full():

        h_1_cards = hand_1[1][::2]
        h_2_cards = hand_2[1][::2]
        h_1_f_three_i = cards_rank.index(re.search(r'.{3}', h_1_cards)[0][0])
        h_2_f_three_i = cards_rank.index(re.search(r'.{3}', h_2_cards)[0][0])
        if h_1_f_three_i < h_2_f_three_i:
            result['gracz_1'] += 1
        elif h_1_f_three_i > h_2_f_three_i:
            result['gracz_2'] += 1
        else:
            h_1_f_pair = cards_rank.index(re.search(r'.{2}', h_1_cards)[0][0])
            h_2_f_pair = cards_rank.index(re.search(r'.{2}', h_2_cards)[0][0])
            check(h_1_f_pair, h_2_f_pair, check_all)

    h_1_0 = hand_1[0]
    h_2_0 = hand_2[0]
    if h_1_0 < h_2_0:
        result['gracz_1'] += 1
    elif h_1_0 > h_2_0:
        result['gracz_2'] += 1
    elif h_1_0 == h_2_0:
        if h_1_0 == 9:
            check_all()
        elif h_1_0 == 3:
            check_full()
        else:
            h_1_1_0_i = cards_rank.index(hand_1[1][0])
            h_2_1_0_i = cards_rank.index(hand_2[1][0])
            if h_1_1_0_i < h_2_1_0_i:
                result['gracz_1'] += 1
            elif h_1_1_0_i > h_2_1_0_i:
                result['gracz_2'] += 1
            elif h_1_0 == 7:
                h_1_1_3_i = cards_rank.index(hand_1[1][3])
                h_2_1_3_i = cards_rank.index(hand_2[1][3])
                check(h_1_1_3_i, h_2_1_3_i, check_all)
            else:
                check_all()
    return result


result = {'gracz_1': 0, 'gracz_2': 0}

with open(PATH) as file:
    for line in file:
        hands = line.replace('\n', '').split(' ')
        hand_1 = find_hand(sort_hand(hands[:5]))
        hand_2 = find_hand(sort_hand(hands[5:]))
        result = compare(hand_1, hand_2, result)

print(result)


def test_find_pattern():

    # poker_krolewski:
    assert find_hand('AHKHQHJHTH')[0] == 0

    # poker:
    assert find_hand('KHQHJHTH9H')[0] == 1

    # kareta:
    assert find_hand('AHADACASJS')[0] == 2
    assert find_hand('AHJDJCJSJH')[0] == 2

    # full:
    assert find_hand('AHADAS2H2D')[0] == 3
    assert find_hand('AHAD2S2H2D')[0] == 3

    # kolor:
    assert find_hand('AHQHJHTH9H')[0] == 4

    # street:
    assert find_hand('JHTD9C8S7H')[0] == 5

    # trojka:
    assert find_hand('AHADAC2SJS')[0] == 6
    assert find_hand('AHKDKCKHJS')[0] == 6
    assert find_hand('AHKDQCQHQS')[0] == 6

    # dwie_pary:
    assert find_hand('AHKHKD3H3D')[0] == 7
    assert find_hand('AHADKDKC2S')[0] == 7
    assert find_hand('AHADKSQDQC')[0] == 7

    # para:
    assert find_hand('AHKDKDQC2S')[0] == 8
    assert find_hand('AHKDJD3C3S')[0] == 8
    assert find_hand('AHKDJD3C3S')[0] == 8

    # pusta:
    assert find_hand('ASKHQHJH2H')[0] == 9


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
        [3, 'AHADKHKDKS', 'AHADKHKDKS'],
        [3, 'ACASTHTDTS', 'ACASTHTDTS'],
        result.copy()
    )
    assert resp == desired_resp

    resp = compare(
        [3, 'ACASTHTDTS', 'ACASTHTDTS'],
        [3, 'KCKSTHTDTS', 'KCKSTHTDTS'],
        result.copy()
    )
    assert resp == desired_resp

    resp = compare(
        [3, 'AHADKHKDKS', 'AHADKHKDKS'],
        [3, 'AHADKHKDKS', 'AHADKHKDKS'],
        result.copy()
    )
    assert resp == {'gracz_1': 0, 'gracz_2': 0}

    resp = compare(
        [8, 'AHKDJS2H2D', 'KHQD5S2H2D'],
        [8, 'KHKD2S2H2D', 'KHKD2S2H2D'],
        result.copy()
    )
    assert resp == desired_resp
