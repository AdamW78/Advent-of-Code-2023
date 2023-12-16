POSS_NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_num_at_index(string_to_index, index_num) -> int:
    if string_to_index[index_num].isdigit():
        return int(string_to_index[index_num])
    else:
        build_a_str = ""
        while build_a_str not in POSS_NUMBERS[10:]:
            build_a_str += string_to_index[index_num]
            index_num += 1
        for i, string_num in enumerate(POSS_NUMBERS[10:]):
            if build_a_str == string_num:
                return i


line_nums = list()
with (open('input', 'rt', encoding='utf8') as input_file):
    read_line = input_file.readline().strip('\n')
    while read_line:
        minIndexLeft = len(read_line)
        minIndexRight = len(read_line)
        for index, number in enumerate(POSS_NUMBERS):
            search_result = read_line.find(number)
            if search_result != -1:
                minIndexLeft = min(minIndexLeft, search_result)
            # print(f"Search String Right: {read_line[::-1]}")
            # print(f"Search Substring Right: {number[::-1]}")
            # print(f"Search Result Right: {read_line[::-1].find(number[::-1])}")
            search_result = read_line[::-1].find(number[::-1])
            if search_result != -1:
                minIndexRight = min(minIndexRight, search_result + len(number) - 1)
        maxIndex = (len(read_line) - 1) - minIndexRight
        num1 = get_num_at_index(read_line, minIndexLeft)
        num2 = get_num_at_index(read_line, maxIndex)
        line_num = int(f"{num1}{num2}")
        line_nums.append(line_num)
        read_line = input_file.readline().strip('\n')

print(sum(line_nums))
