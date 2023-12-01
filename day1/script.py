sum = 0
valid_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
valid_strings_reversed = [s[::-1] for s in valid_strings]

def find_first_digit_in_string(line: str, valid_strings) -> str:
    word = ''
    for c in line:
        if c.isnumeric():
            return (str)(c)
        word += c
        for i, valid in enumerate(valid_strings):
            if valid in word:
                return (str)(i + 1)
            

with open('./data.txt') as f:
    for line in f.readlines():
        first_digit = find_first_digit_in_string(line, valid_strings)
        last_digit  = find_first_digit_in_string(line[::-1], valid_strings_reversed)
        sum += (int)(first_digit + last_digit)


print(sum)
            