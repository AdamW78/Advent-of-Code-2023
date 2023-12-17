import string
list()

input_array = None
with open('input', 'rt', encoding='utf8') as input_file:
    input_array = input_file.readlines()

total_sum = 0
for line_number, line in enumerate(input_array):
    for char_number, char in enumerate(line):
        if char == '*':
            found_nums = list()
            for i in range(line_number - 1, line_number + 2):
                j = char_number - 1
                while char_number - 1 <= j <= char_number + 1:
                    if 0 <= i < len(input_array) and 0 <= j < len(line):
                        if input_array[i][j].isdigit():
                            u = q = j
                            while input_array[i][q - 1].isdigit():
                                q -= 1
                            while input_array[i][u + 1].isdigit():
                                u += 1
                            created_num = int(input_array[i][q:u+1])
                            found_nums.append(created_num)
                            j = u
                    j += 1
            if len(found_nums) == 2:
                total_sum += found_nums[0] * found_nums[1]
print(total_sum)


