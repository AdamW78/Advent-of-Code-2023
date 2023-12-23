"""
Shared code for https://adventofcode.com/2023/day/7
"""
import sys
from collections import namedtuple
from typing import List

Hand = namedtuple('Hand', 'cards bet type')

FIVE_OF_KIND = 0
FOUR_OF_KIND = 1
FULL_HOUSE = 2
THREE_OF_KIND = 3
TWO_PAIR = 4
ONE_PAIR = 5
HIGH_CARD = 6
CARD_SUITS_JACK = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')
CARD_SUITS_JOKER = ('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J')


def compare_suits_joker(hand_a: Hand, hand_b: Hand) -> int:
    """
    Comparison function used to compare the suits of the cards between two hands
    :param hand_a: The first hand to have its cards' suits compared.
    :param hand_b: The second hand to have its cards' suits compared.
    :return: Zero if the suits are the same, -1 if suit A beats suit B, 1 otherwise.
    """
    suit_a = hand_a.cards
    suit_b = hand_b.cards
    if suit_a == suit_b:
        return 0
    for i, _ in enumerate(suit_a):
        suit_a_index = CARD_SUITS_JOKER.index(suit_a[i])
        suit_b_index = CARD_SUITS_JOKER.index(suit_b[i])
        if suit_a_index > suit_b_index:
            return 1
        if suit_a_index < suit_b_index:
            return -1
    sys.exit(f"Failed to compare two cards: {hand_a} and {hand_b}.")


def compare_suits_jack(hand_a: Hand, hand_b: Hand) -> int:
    """
    Comparison function used to compare the suits of the cards between two hands
    :param hand_a: The first hand to have its cards' suits compared.
    :param hand_b: The second hand to have its cards' suits compared.
    :return: Zero if the suits are the same, -1 if suit A beats suit B, 1 otherwise.
    """
    suit_a = hand_a.cards
    suit_b = hand_b.cards
    if suit_a == suit_b:
        return 0
    for i, _ in enumerate(suit_a):
        suit_a_index = CARD_SUITS_JACK.index(suit_a[i])
        suit_b_index = CARD_SUITS_JACK.index(suit_b[i])
        if suit_a_index > suit_b_index:
            return 1
        if suit_a_index < suit_b_index:
            return -1
    sys.exit(f"Failed to compare two cards: {hand_a} and {hand_b}.")


def get_hand_type(cards: str, jokers=False) -> int:  # pylint: disable=too-many-return-statements
    """
    Returns the type of hand that a given set of cards is
    :param cards: A string of five card suits (characters)
    :return:  The type of hand that a given set of cards is
    """
    card_nums = {}
    for card in cards:
        if card not in card_nums:
            card_nums[card] = 1
        else:
            card_nums[card] += 1
    max_card_num = max(card_nums.values())
    if jokers and 'J' in card_nums:
        if card_nums['J'] == 5:
            return FIVE_OF_KIND
        num_jokers = card_nums['J']
        if num_jokers == max_card_num:
            del card_nums['J']
            max_card_num = max(card_nums.values())
        max_card_num += num_jokers
        replace_max = max(card_nums.values())
        most_freq_card = None
        for card, num_apps in card_nums.items():
            if num_apps == replace_max:
                most_freq_card = card
        card_nums[most_freq_card] = max_card_num

    match max_card_num:
        case 5:
            return FIVE_OF_KIND
        case 4:
            return FOUR_OF_KIND
        case 3:
            if 2 in card_nums.values():
                return FULL_HOUSE
            return THREE_OF_KIND
        case 2:
            found_twos = 0
            for card_num in card_nums.values():
                if card_num == 2 and found_twos:
                    return TWO_PAIR
                if card_num == 2:
                    found_twos += 1
            return ONE_PAIR
        case 1:
            return HIGH_CARD


def get_hands(file='example_input', jokers=False) -> List[Hand]:
    """
    Read in input to namedtuple Hand containing a string cards and an int bet
    :param file: input file to read hands from, defaults to 'example_input'
    :return:
    """
    with open(file, 'rt', encoding='utf8') as inp:
        hands = []
        line = inp.readline()
        while line:
            line = line.strip('\n').split(' ')
            line[1] = int(line[1])
            hand_type = get_hand_type(line[0])
            if jokers:
                hand_type = get_hand_type(line[0], jokers)
            hands.append(Hand(line[0], line[1], hand_type))
            line = inp.readline()
    return hands
