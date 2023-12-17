"""
https://adventofcode.com/2023/day/3#day-desc
"""
import string
from read_input import read

INPUT_ARR = read()

TOTAL_SUM = 0
for line_number, line in enumerate(INPUT_ARR):
    CUR_NUM = ""
    for char_number, char in enumerate(line):
        if char.isdigit():
            CUR_NUM += char
        elif char in ('.', '\n'):
            NUM_DIGITS = len(CUR_NUM)
            FOUND = False
            if CUR_NUM != '':
                for i in range(line_number - 1, line_number + 2):
                    for k in range(char_number - NUM_DIGITS - 1, char_number + 1):
                        if (0 <= i < len(INPUT_ARR)) and (0 <= k < len(line)):
                            if INPUT_ARR[i][k] != '.' and INPUT_ARR[i][k] in string.punctuation:
                                FOUND = True
            if FOUND:
                TOTAL_SUM += int(CUR_NUM)
            CUR_NUM = ""
        else:
            if CUR_NUM != "":
                TOTAL_SUM += int(CUR_NUM)
                CUR_NUM = ""
print(TOTAL_SUM)
