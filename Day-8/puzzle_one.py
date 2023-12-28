"""
https://adventofcode.com/2023/day/8#day-desc
"""
from typing import Tuple

from desert import Node, read_desert_map, dirs


def navigate_desert(directions: str, desert_map: Tuple[Node, ...], start: Node) -> int:
    """
    Navigate desert given a desert map and a set of directions.
    :param dest: Destination node - once this node has been arrived at, we are done!
    :param start: Source node - this is where we start from!
    :param directions: String containing L and R directions to follow.
    :param desert_map: Tuple of nodes - each node has left and right child.
    :return: Integer number of steps it took to get to the final node.
    """
    dir_index = 0
    steps_taken = 0
    cur_node = start
    while cur_node.label != 'ZZZ':
        match dirs.get(directions[dir_index]):
            case 0:  # LEFT
                cur_node = desert_map[cur_node.left]
            case 1:  # RIGHT
                cur_node = desert_map[cur_node.right]
            case _:  # NEITHER LEFT NOR RIGHT
                raise RuntimeError(f"Error: Invalid direction at index {dir_index} "
                                   f"in direction string {directions}")
        steps_taken += 1
        if dir_index == len(directions) - 1:
            dir_index = 0
        else:
            dir_index += 1
    return steps_taken


d_map = read_desert_map('input')
dirs = d_map[0]
s = d_map[2]
d_map = d_map[1]
STEPS = navigate_desert(dirs, d_map, s)
print(STEPS)
