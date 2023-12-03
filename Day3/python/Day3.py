from math import prod

from common.common import path


def sum_part_numbers(grid):
    SYMBOLS = "!@#$%^&*()_+-=][{}|:;/?<>"
    sum = 0

    def extract_number(i, j):
        num_str = grid[i][j]
        k = 1
        while j + k < len(grid[0]) and grid[i][j + k].isdigit():
            num_str += grid[i][j + k]
            k += 1
        return int(num_str), j + k - 1

    def is_adjacent_to_symbol(i, j_start, j_end):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                for j in range(j_start, j_end + 1):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] in SYMBOLS:
                        return True
        return False

    for i, row in enumerate(grid):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                num, j_end = extract_number(i, j)
                if is_adjacent_to_symbol(i, j, j_end):
                    sum += num
                j = j_end
            j += 1
    return sum


def sum_gear_ratios(grid):
    SYMBOL = "*"
    gears = {}
    sum_of_gears = 0

    def extract_number(i, j):
        num_str = grid[i][j]
        k = 1
        while j + k < len(grid[0]) and grid[i][j + k].isdigit():
            num_str += grid[i][j + k]
            k += 1
        return int(num_str), j + k - 1

    def update_gears(i, j, num):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == SYMBOL:
                    gears.setdefault((ni, nj), set()).add(num)

    for i, row in enumerate(grid):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                num, j_end = extract_number(i, j)
                update_gears(i, j, num)
                update_gears(i, j_end, num)
                j = j_end
            j += 1
    for gear_nums in gears.values():
        if len(gear_nums) == 2:
            sum_of_gears += prod(gear_nums)

    return sum_of_gears


def part_1(file):
    matrix = []
    data = path(file, "Day3")
    for entry in data:
        a = list(entry)
        matrix.append(a)
    return sum_part_numbers(matrix)


def part_2(file):
    matrix = []
    data = path(file, "Day3")
    for entry in data:
        a = list(entry)
        matrix.append(a)
    return sum_gear_ratios(matrix)


if __name__ == '__main__':
    print(f"Part 1:{part_1('part1.txt')}")
    print(f"Part 2:{part_2('part1.txt')}")
