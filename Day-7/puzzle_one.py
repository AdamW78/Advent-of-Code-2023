"""
https://adventofcode.com/2023/day/7#day-desc
"""
from functools import cmp_to_key

from camel_cards import get_hands, compare_suits


def find_total_winnings() -> int:
    """
    Find the numerical total of winnings as described by the puzzle-given hands
    :return: Total winnings, as an integer
    """
    winnings = 0
    hands = get_hands('input')
    # Sort purely based on suits in cards
    hands = sorted(hands, key=cmp_to_key(compare_suits))
    # Maintaining the above order (wherever possible), sort based on type of hand
    hands = sorted(hands, key=lambda card: card.type, reverse=True)
    rank = len(hands)
    for hand in hands:
        winnings += rank * hand.bet
        rank -= 1
    return winnings


print(find_total_winnings())
