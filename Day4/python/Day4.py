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
    cards = [([int(num) for num in part.split() if num.isdigit()] for part in line.strip().split('|')) for line in data]
    games = [1 for _ in cards]
    for i in range(len(cards)):
        winning_nums, ticket_nums = cards[i]
        matches = len(set(winning_nums) & set(ticket_nums))
        for j in range(matches):
            if i + j + 1 < len(cards):
                games[i + j + 1] += games[i]
    return sum(games)


if __name__ == '__main__':
    print(f"Part 1:{part_1('day4input.txt')}")
    print(f"Part 2:{part_2('day4input.txt')}")
