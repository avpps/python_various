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


PATH = 'C://repositories//files//poker_1.txt'
ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
SCHEMES = dict(
    blank='H',
    pair='SaSa',
    three='SaSaSa',
    street='FaNaNaNaNa',
    colour='AsAsAsAsAs',
    kareta='SaSaSaSa',
    poker='FsNsNsNsNs',
    king_poker=''
)
SCORES = [

]


def sort_hand(hand):
    hand_sorted = sorted(hand, key=lambda x: ORDER.index(x[0]))
    return hand_sorted


def find_pattern(hand):
    hand_aggr = None

    return hand_aggr


def compare(player_1, player_2, result):
    result_updated = None
    return result_updated


result = {'gracz_1': 0, 'gracz_2': 0}

with open(PATH) as file:
    for line in file:
        hands = line.replace('\n', '').split(' ')
        hand_1 = find_pattern(sort_hand(hands[:5]))
        hand_2 = find_pattern(sort_hand(hands[5:]))
        result = compare(hand_1, hand_2, result)

print(result['gracz_1'])
