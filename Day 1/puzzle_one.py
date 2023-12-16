nums = list()
with open('input', 'rt', encoding='utf8') as input_file:
    read_line = input_file.readline()
    while read_line:
        c1 = None
        index = 0
        while c1 is None:
            c = read_line[index]
            if c.isdigit():
                c1 = c
            index += 1
        c2 = None
        index = len(read_line) - 1
        while c2 is None:
            c = read_line[index]
            if c.isdigit():
                c2 = c
            index -= 1
        formed_num = f"{c1}{c2}"
        nums.append(int(formed_num))
        read_line = input_file.readline()
print(sum(nums))
