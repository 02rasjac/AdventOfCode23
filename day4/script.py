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


def find_n_wins(card):
    total_matches = 0
    for won in card[0]:
        if won in card[1]:
            total_matches += 1
    return total_matches


n_of_cards = [1 for x in range(0, len(cards))]
for i, card in enumerate(cards):
    n_wins = find_n_wins(card)
    multiplier = n_of_cards[i] if i > 0 else 1
    for x in range(i + 1, i + n_wins + 1):
        if x < len(n_of_cards):
            n_of_cards[x] += 1 * multiplier

print(sum(n_of_cards))
# print(total)
