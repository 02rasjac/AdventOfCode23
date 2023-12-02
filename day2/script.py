import re

loaded = {"red": 12, "green": 13, "blue": 14}
sum_of_ids = 0
sum_of_powers = 0


def is_valid_game(game):
    for i in range(2, len(game), 2):
        if int(game[i]) > loaded[game[i + 1]]:
            return False
    return True


def calculate_power(game):
    curr_most = {"red": 0, "green": 0, "blue": 0}
    for i in range(2, len(game), 2):
        if int(game[i]) > curr_most[game[i + 1]]:
            curr_most[game[i + 1]] = int(game[i])
    return curr_most["red"] * curr_most["green"] * curr_most["blue"]


with open("data.txt") as f:
    for line in f.readlines():
        if line == 0:
            break
        cleaned_line = re.sub("[,;\n]", "", line)
        # First index is ignorable. Second index is the game-ID. After that, every even index is the number of cubes, followed by which color it is.
        splitted = cleaned_line.split(" ")
        sum_of_powers += calculate_power(splitted)

print(sum_of_powers)
