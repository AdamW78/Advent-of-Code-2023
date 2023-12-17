"""
https://adventofcode.com/2023/day/1#day-desc
"""
nums = []
with open('input', 'rt', encoding='utf8') as input_file:
    read_line = input_file.readline()
    while read_line:
        C1 = None
        INDEX = 0
        while C1 is None:
            C = read_line[INDEX]
            if C.isdigit():
                C1 = C
            INDEX += 1
        C2 = None
        INDEX = len(read_line) - 1
        while C2 is None:
            C = read_line[INDEX]
            if C.isdigit():
                C2 = C
            INDEX -= 1
        formed_num = f"{C1}{C2}"
        nums.append(int(formed_num))
        read_line = input_file.readline()
print(sum(nums))
