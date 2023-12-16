from typing import List


class CubeDraw:
    def __init__(self):
        self.red = -1
        self.green = -1
        self.blue = -1

    def __str__(self):
        return f"Red Cubes: {self.red}, Green Cubes: {self.green}, Blue Cubes: {self.blue}"


def get_cube_draw(drawn_cube_string: List[str]) -> CubeDraw:
    return_cube_draw = CubeDraw()
    for cube_set in drawn_cube_string:
        red_find = cube_set.rfind("red")
        green_find = cube_set.rfind("green")
        if red_find > 0:
            return_cube_draw.red = int(cube_set[:cube_set.index(" ")])
        elif green_find > 0:
            return_cube_draw.green = int(cube_set[:cube_set.index(" ")])
        else:
            return_cube_draw.blue = int(cube_set[:cube_set.index(" ")])
    return return_cube_draw
