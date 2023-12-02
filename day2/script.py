import re

loaded = {"red": 12, "green": 13, "blue": 14}
sum_of_ids = 0


def is_valid_game(game):
    for i in range(2, len(game), 2):
        if int(game[i]) > loaded[game[i + 1]]:
            return False
    return True


with open("data.txt") as f:
    for line in f.readlines():
        cleaned_line = re.sub("[,;\n]", "", line)
        # First index is ignorable. Second index is the game-ID. After that, every even index is the number of cubes, followed by which color it is.
        splitted = cleaned_line.split(" ")

        if is_valid_game(splitted):
            sum_of_ids += int(splitted[1][:-1])

print(sum_of_ids)
