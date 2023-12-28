"""
https://adventofcode.com/2023/day/8#day-desc
"""
from collections import namedtuple
from typing import Tuple

Node = namedtuple('Node', 'label left right')
dirs = {'L': 0, 'R': 1}


def read_desert_map(file='example_input_one') -> Tuple[str, Tuple[Node, ...], Node, Node]:
    """
    Read in input to a list of nodes that make up the desert map
    :param file: File from which to read input
    :return: Tuple of nodes - desert map
    """
    with open(file, 'rt', encoding='utf8') as inp:
        dir_str = inp.readline().rstrip('\n')
        # Read blank line
        inp.readline()
        # Read nodes in desert map input
        cur_node_raw = inp.readline()
        node_network = []
        while cur_node_raw:
            cur_node_raw = cur_node_raw.rstrip('\n').split(" = ")
            lr = cur_node_raw[1].strip('(').rstrip(')').split(', ')
            cur_node = [cur_node_raw[0], lr[0], lr[1]]
            node_network.append(cur_node)
            cur_node_raw = inp.readline()
        start_node = None
        dest_node = None
        for i, node in enumerate(node_network):
            if node[1] == node[0]:
                node_network[i][1] = i
            if node[2] == node[0]:
                node_network[i][2] = i
            j = i + 1
            q = i - 1
            while isinstance(node_network[i][1], str) or isinstance(node_network[i][2], str):
                if j < len(node_network) and node_network[j][0] == node[1]:
                    node_network[i][1] = j
                if j < len(node_network) and node_network[j][0] == node[2]:
                    node_network[i][2] = j
                if q >= 0 and node_network[q][0] == node[1]:
                    node_network[i][1] = q
                if q >= 0 and node_network[q][0] == node[2]:
                    node_network[i][2] = q
                j += 1
                q -= 1
            node_network[i] = Node(*node)
            if node_network[i].label == 'AAA':
                start_node = node_network[i]
            elif node_network[i].label == 'ZZZ':
                dest_node = node_network[i]
        return dir_str, tuple(node_network), start_node, dest_node


def navigate_desert(directions: str, desert_map: Tuple[Node, ...], start: Node, dest: Node) -> int:
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
    while cur_node != dest:
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
d = d_map[0]
s = d_map[2]
des = d_map[3]
d_map = d_map[1]
STEPS = navigate_desert(d, d_map, s, des)
print(STEPS)
