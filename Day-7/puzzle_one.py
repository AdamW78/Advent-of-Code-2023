"""
https://adventofcode.com/2023/day/7#day-desc
"""
from functools import cmp_to_key
from operator import attrgetter

from camel_cards import get_hands, compare_suits_jack


def find_total_winnings() -> int:
    """
    Find the numerical total of winnings as described by the puzzle-given hands
    :return: Total winnings, as an integer
    """
    winnings = 0
    hands = get_hands('input')
    # Initial sort - based on ranking of each card in each hand
    # First card is the most important one
    # K is before Q, Q is before J, J is before T, etc.
    hands.sort(key=cmp_to_key(compare_suits_jack))
    # Maintaining the above order (wherever possible), sort based on type of hand
    hands.sort(key=attrgetter('type'))
    rank = len(hands)
    for hand in hands:
        winnings += rank * hand.bet
        rank -= 1
    return winnings


print(find_total_winnings())
