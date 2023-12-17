"""
https://adventofcode.com/2023/day/3#part2
"""
from read_input import read

INPUT_ARR = read()

TOTAL_SUM = 0
for line_number, line in enumerate(INPUT_ARR):
    for char_number, char in enumerate(line):
        if char == '*':
            found_nums = []
            for i in range(line_number - 1, line_number + 2):
                j = char_number - 1
                while char_number - 1 <= j <= char_number + 1:
                    if 0 <= i < len(INPUT_ARR) and 0 <= j < len(line):
                        if INPUT_ARR[i][j].isdigit():
                            u = q = j
                            while INPUT_ARR[i][q - 1].isdigit():
                                q -= 1
                            while INPUT_ARR[i][u + 1].isdigit():
                                u += 1
                            created_num = int(INPUT_ARR[i][q:u + 1])
                            found_nums.append(created_num)
                            j = u
                    j += 1
            if len(found_nums) == 2:
                TOTAL_SUM += found_nums[0] * found_nums[1]
print(TOTAL_SUM)
