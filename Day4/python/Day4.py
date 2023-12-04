from common.common import path


def part_1(file):
    data = path(file, "Day4")
    cleaned_data = [line.strip() for line in data]
    score = 0
    for line in cleaned_data:
        parts = line.split('|')
        winning_nums = [int(num) for num in parts[0].split() if num.isdigit()]
        ticket_nums = [int(num) for num in parts[1].split() if num.isdigit()]
        current_score = 0
        for num in winning_nums:
            if num in ticket_nums:
                current_score = 1 if current_score == 0 else current_score * 2
        score += current_score
    return score


def part_2(file):
    data = path(file, "Day4")
    cards = [line.strip() for line in data]
    cards = [(line.split('|')[0].split(), line.split('|')[1].split()) for line in cards]
    cards = [([int(num) for num in card[0] if num.isdigit()], [int(num) for num in card[1] if num.isdigit()]) for card
             in cards]
    games = [1 for _ in cards]
    for i in range(len(cards)):
        winning_nums, ticket_nums = cards[i]
        matches = len(set(winning_nums) & set(ticket_nums))
        for j in range(matches):
            if i + j + 1 < len(cards):
                games[i + j + 1] += games[i]
    return sum(games)


if __name__ == '__main__':
    print(f"Part 1:{part_1('part1.txt')}")
    print(f"Part 2:{part_2('part1.txt')}")
