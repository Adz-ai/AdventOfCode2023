from collections import Counter

import pandas as pd

from common.common import get_path

CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def translate(card):
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    return card_values.get(card, int(card)) if card.isdigit() else card_values[card]


def translate_part_two(card):
    """ Translates card labels to numerical values for Part 2, treating J as the weakest. """
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, 'J': 1}  # J is now the weakest
    return card_values.get(card, int(card)) if card.isdigit() else card_values[card]


def find_type(cards):
    count = Counter(cards)
    unique_counts = frozenset(count.values())
    type_mapping = {
        (1, frozenset({5})): 1,
        (2, frozenset({4, 1})): 2,
        (2, frozenset({3, 2})): 3,
        (3, frozenset({3, 1})): 4,
        (3, frozenset({2, 1})): 5,
        (4, frozenset({2, 1})): 6,
    }
    return type_mapping.get((len(count.keys()), unique_counts), 7)


def find_type_part_two(cards):
    count = Counter(cards)
    joker_count = count.pop('J', 0)

    best_type = 7
    for card in CARDS:
        temp_count = count.copy()
        temp_count[card] += joker_count  # Add jokers as the current card
        unique_counts = frozenset(temp_count.values())

        type_mapping = {
            (1, frozenset({5})): 1,
            (2, frozenset({4, 1})): 2,
            (2, frozenset({3, 2})): 3,
            (3, frozenset({3, 1})): 4,
            (3, frozenset({2, 1})): 5,
            (4, frozenset({2, 1})): 6,
        }
        possible_type = type_mapping.get((len(temp_count.keys()), unique_counts), 7)
        best_type = min(best_type, possible_type)

    return best_type


def part_2(file):
    df = pd.read_csv(get_path("Day7", file), sep=' ', header=None, names=['cards', 'bid'])
    df['type'] = df['cards'].apply(find_type_part_two)
    for i in range(5):
        df[f'card{i}'] = df['cards'].apply(lambda x, i=i: translate_part_two(x[i]))
    df = df.sort_values(by=['type', 'card0', 'card1', 'card2', 'card3', 'card4'],
                        ascending=[False, True, True, True, True, True])
    df = df.reset_index(drop=True)
    df['winning'] = df['bid'] * (df.index + 1)
    total_winnings = df['winning'].sum()
    return total_winnings


def part_1(file):
    df = pd.read_csv(get_path("Day7", file), sep=' ', header=None, names=['cards', 'bid'])
    df['type'] = df['cards'].apply(find_type)
    for i in range(5):
        df[f'card{i}'] = df['cards'].apply(lambda x, i=i: translate(x[i]))
    df = df.sort_values(by=['type', 'card0', 'card1', 'card2', 'card3', 'card4'],
                        ascending=[False, True, True, True, True, True])
    df = df.reset_index(drop=True)
    df['winning'] = df['bid'] * (df.index + 1)
    total_winnings = df['winning'].sum()
    return total_winnings


if __name__ == '__main__':
    print(f"Part 1:{part_1('part1.txt')}")
    print(f"Part 2: {part_2('part1.txt')}")
