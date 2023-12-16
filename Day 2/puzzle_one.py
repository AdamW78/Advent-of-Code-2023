from typing import List


class CubeDraw:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f"Red Cubes: {self.red}, Green Cubes: {self.green}, Blue Cubes: {self.blue}"


def get_cube_draw(cube_draw: List[str]):
    for cube_set in cube_draw:
        print(cube_set)


raw_data = []
with open('input', 'rt', encoding='utf8') as input_file:
    raw_data = input_file.readlines()

games = [len(raw_data)]
for line_number, line in enumerate(raw_data):
    print(line_number, line)
    line = line.rstrip('\n')
    line = line[line.index(': ') + 2:]
    line = line.split('; ')
    for cube_draw in line:
        get_cube_draw(cube_draw.split(', '))
