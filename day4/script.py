import os

cards = []
total = 0
with open(os.path.join(os.path.dirname(__file__), "./data.txt")) as f:
    for line in f.readlines():
        # Remove the card-id
        start_index = line.find(":")
        only_numbers = line[start_index + 2 :][:-1]
        split_between_won_and_had = only_numbers.split("|")
        # Extract only numebrs
        won_numbers = split_between_won_and_had[0].split()
        had_numbers = split_between_won_and_had[1].split()
        cards.append([won_numbers, had_numbers])

for card in cards:
    total_matches = 0
    for won in card[0]:
        if won in card[1]:
            total_matches += 1
    total += pow(2, (total_matches - 1)) if total_matches > 0 else 0


print(total)
