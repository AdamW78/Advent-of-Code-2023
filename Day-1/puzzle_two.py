"""
https://adventofcode.com/2023/day/1#part2
"""

POSS_NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_num_at_index(string_to_index, index_num) -> int:
    """
    Used to fetch an integer, represented either as a string or an int-literal, from POSS_NUMBERS
    """
    if string_to_index[index_num].isdigit():
        return int(string_to_index[index_num])
    build_a_str = ""
    while build_a_str not in POSS_NUMBERS[10:]:
        build_a_str += string_to_index[index_num]
        index_num += 1
    for i, string_num in enumerate(POSS_NUMBERS[10:]):
        if build_a_str == string_num:
            return i
    return -1  # Unreachable code


line_nums = []
with open('input', 'rt', encoding='utf8') as input_file:
    read_line = input_file.readline().strip('\n')
    while read_line:
        min_index, max_index = len(read_line), -1
        for index, number in enumerate(POSS_NUMBERS):
            search_result = read_line.find(number)
            if search_result != -1:
                min_index = min(min_index, search_result)
            search_result = read_line[::-1].find(number[::-1])
            if search_result != -1:
                max_index = max(max_index, (len(read_line) - 1) - (search_result + len(number) - 1))
        num1 = get_num_at_index(read_line, min_index)
        num2 = get_num_at_index(read_line, max_index)
        line_num = int(f"{num1}{num2}")
        line_nums.append(line_num)
        read_line = input_file.readline().strip('\n')
print(sum(line_nums))
