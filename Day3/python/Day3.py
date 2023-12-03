from common.common import path


def sum_part_numbers(grid):
    SYMBOLS = "!@#$%^&*()_+-=][{}|:;/?<>"
    total_sum = 0
    for i, row in enumerate(grid):
        index = 0
        while index < len(row):
            if row[index].isdigit():
                num_str, positions = row[index], [index]
                index += 1
                while index < len(row) and row[index].isdigit():
                    num_str += row[index]
                    positions.append(index)
                    index += 1
                num = int(num_str)
                adjacent_chars = []
                if positions[0] != 0:
                    adjacent_chars.append(grid[i][positions[0] - 1])
                if positions[-1] + 1 < len(row):
                    adjacent_chars.append(grid[i][positions[-1] + 1])
                for pos in positions:
                    if i != 0:
                        adjacent_chars.append(grid[i - 1][pos])
                    if i + 1 < len(grid):
                        adjacent_chars.append(grid[i + 1][pos])
                if positions[0] != 0 and i != 0:
                    adjacent_chars.append(grid[i - 1][positions[0] - 1])
                if positions[-1] + 1 < len(row) and i != 0:
                    adjacent_chars.append(grid[i - 1][positions[-1] + 1])
                if positions[0] != 0 and i + 1 < len(grid):
                    adjacent_chars.append(grid[i + 1][positions[0] - 1])
                if positions[-1] + 1 < len(row) and i + 1 < len(grid):
                    adjacent_chars.append(grid[i + 1][positions[-1] + 1])
                if any(char in SYMBOLS for char in adjacent_chars):
                    total_sum += num
            else:
                index += 1
    return total_sum


def sum_gear_ratios(grid):
    SYMBOL = "*"
    gears = {}
    sum_of_gear_ratios = 0
    for i, row in enumerate(grid):
        index = 0
        while index < len(row):
            if row[index].isnumeric():
                positions = []
                num = row[index]
                positions.append(index)
                index += 1
                while index < len(row) and row[index].isnumeric():
                    num += row[index]
                    positions.append(index)
                    index += 1
                num = int(num)
                adjacent_chars_pos = []
                if positions[0] != 0:
                    adjacent_chars_pos.append((i, positions[0] - 1))
                if positions[0] != 0 and i != 0:
                    adjacent_chars_pos.append((i - 1, positions[0] - 1))
                if positions[-1] + 1 != len(row) and i != 0:
                    adjacent_chars_pos.append((i - 1, positions[-1] + 1))
                if positions[-1] + 1 != len(row):
                    adjacent_chars_pos.append((i, positions[-1] + 1))
                if positions[-1] + 1 != len(row) and i + 1 != len(grid):
                    adjacent_chars_pos.append((i + 1, positions[-1] + 1))
                if positions[0] != 0 and i + 1 != len(grid):
                    adjacent_chars_pos.append((i + 1, positions[0] - 1))
                if len(positions) == 1:
                    if i != 0:  # above
                        adjacent_chars_pos.append((i - 1, positions[0]))
                    if i + 1 != len(grid):  # below
                        adjacent_chars_pos.append((i + 1, positions[0]))
                elif len(positions) > 1:
                    if i != 0:
                        adjacent_chars_pos.extend([(i - 1, pos) for pos in positions])
                    if i + 1 != len(grid):  # below
                        adjacent_chars_pos.extend([(i + 1, pos) for pos in positions])
                for pos in adjacent_chars_pos:
                    if grid[pos[0]][pos[1]] == SYMBOL:
                        if pos in gears:
                            gears[pos].append(num)
                        else:
                            gears[pos] = [num]
            else:
                index += 1
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio = nums[0] * nums[1]
            sum_of_gear_ratios += gear_ratio
    return sum_of_gear_ratios


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
