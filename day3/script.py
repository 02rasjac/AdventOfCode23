# Part 1: 525119
# Parse data into a list of lines.
# FOR EACH LINE
#   Find the index of the start of a number.
#   Find the index of the end of that number
#   Check the line before current line at index `start - 1` to `end + 1` for a
#       symbol
#   Do the same thing for the next line
#   IF symbol is found:
#       Add that number to the sum

import os
import re

# Regex to find if a string includes something other than numbers or periods
reg = re.compile(r"[^0-9.]")

# List of all lines
data = []
sum_of_nums = 0
with open(os.path.join(os.path.dirname(__file__), "./data.txt")) as f:
    for line in f.readlines():
        data.append(line[:-1])


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


for i, line in enumerate(data):
    start_index = -1
    end_index = -1
    for j, c in enumerate(line):
        is_num = c.isnumeric()

        if start_index < 0 and is_num:
            # See if we found the start of a number
            start_index = j
        elif start_index >= 0 and (not is_num or j == len(line) - 1):
            # See if we found the end of a number
            if j == len(line) - 1 and is_num:
                end_index = j
            else:
                end_index = j - 1
            if check_for_symbols(i, start_index, end_index):
                sum_of_nums += int(line[start_index : end_index + 1])
            start_index = -1
            end_index = -1

print(sum_of_nums)
