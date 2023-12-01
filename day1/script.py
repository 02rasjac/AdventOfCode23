def seperate_line(line: str):
    """Seperate a string into an array of strings of letters or a digit"""
    word = ''
    arr = []
    for c in line:
        if not c.isnumeric():
            if c == '\n':
                arr.append(word)
            word += c
                
        else:
            if word:
                arr.append(word)
                word = ''
            arr.append(c)
    return arr


sum = 0
valid_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('./data_ex.txt') as f:
    for line in f.readlines():
        seperated = seperate_line(line)
        print(seperated)

print(sum)

# Seperate line into array of "words" and digits
# Find the first and last word or digit that is valid


            