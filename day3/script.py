# Part 1: 525119

# Part 2: 76504829

import os
import re

# Regex to find if a string includes something other than numbers or periods
reg = re.compile(r"[^0-9.]")

# List of all lines
data = []
sum_of_nums = 0
sum_of_ratios = 0
with open(os.path.join(os.path.dirname(__file__), "./data.txt")) as f:
    for line in f.readlines():
        data.append(line[:-1])


class Number:
    line_index = 0
    start_index = 0
    end_index = 0
    length = 0
    number = 0

    def __init__(self, line_index, start_index, length, number) -> None:
        self.line_index = line_index
        self.start_index = start_index
        self.length = length
        self.number = number
        self.end_index = start_index + length - 1

    def printNum(self):
        print(f"{self.line_index} | {self.start_index} | {self.length} | {self.number}")


def check_for_symbols(line_index, start_index, end_index):
    is_before_num = False
    is_after_num = False
    is_before_line = False
    is_after_line = False
    if start_index != 0:
        before_number = data[line_index][start_index - 1]
        is_before_num = bool(reg.search(before_number))
    if end_index != (len(data[line_index]) - 1):
        after_number = data[line_index][end_index + 1]
        is_after_num = bool(reg.search(after_number))
    if start_index == 0:
        start_index = 1
    if end_index >= len(data[line_index]) - 2:
        end_index = len(data[line_index]) - 2

    if line_index > 0:
        # Check line before
        interesting_part = data[line_index - 1][start_index - 1 : end_index + 2]
        is_before_line = bool(reg.search(interesting_part))
    if line_index < len(data) - 1:
        # Check line after
        interesting_part = data[line_index + 1][start_index - 1 : end_index + 2]
        is_after_line = bool(reg.search(interesting_part))

    return is_before_num or is_after_num or is_before_line or is_after_line


# Locate all numbers and gears
numbers = []
gears = []
for i, line in enumerate(data):
    start_index = -1
    number_length = -1
    for j, c in enumerate(line):
        is_num = c.isnumeric()
        if c == "*":
            gears.append([i, j])
        if start_index < 0 and is_num:
            # See if we found the start of a number
            start_index = j
        elif start_index >= 0 and (not is_num or j == len(line) - 1):
            # See if we found the end of a number
            if j == len(line) - 1 and is_num:
                number_length = len(line) - start_index
            else:
                number_length = j - start_index
            numbers.append(
                Number(
                    i,
                    start_index,
                    number_length,
                    line[start_index : (start_index + number_length)],
                )
            )

            start_index = -1
            number_length = -1

# Check if exactly 2 numbers are adjacent to a gear
for gear in gears:
    adjacent_numbers = []
    # Iterate over all numbers in the lines around the gear's line (3 lines total)
    for number in [
        n
        for n in numbers
        if n.line_index >= gear[0] - 1 and n.line_index <= gear[0] + 1
    ]:
        # Check if the number is immedially left of the gear
        is_left = number.end_index == gear[1] - 1
        is_right = number.start_index == gear[1] + 1
        is_on = number.start_index <= gear[1] and number.end_index >= gear[1]
        if is_on or is_left or is_right:
            adjacent_numbers.append(number.number)

    if len(adjacent_numbers) == 2:
        sum_of_ratios += int(adjacent_numbers[0]) * int(adjacent_numbers[1])

print(sum_of_ratios)
