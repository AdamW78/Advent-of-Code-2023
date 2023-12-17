import string

input_array = None
with open('input', 'rt', encoding='utf8') as input_file:
    input_array = input_file.readlines()

total_sum = 0
for line_number, line in enumerate(input_array):
    cur_num = ""
    for char_number, char in enumerate(line):
        if char.isdigit():
            cur_num += char
        elif char == '.' or char == '\n':
            num_digits = len(cur_num)
            found_symbol = False
            if cur_num != '':
                for i in range(line_number - 1, line_number + 2):
                    for k in range(char_number - num_digits - 1, char_number + 1):
                        if (0 <= i < len(input_array)) and (0 <= k < len(line)):
                            if input_array[i][k] != '.' and input_array[i][k] in string.punctuation:
                                found_symbol = True
            if found_symbol:
                total_sum += int(cur_num)
            cur_num = ""
        else:
            if cur_num != "":
                total_sum += int(cur_num)
                cur_num = ""
print(total_sum)


