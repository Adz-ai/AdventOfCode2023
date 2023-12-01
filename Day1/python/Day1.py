import os.path
from pathlib import Path

from word2number import w2n


def path(file):
    base_path = os.path.dirname(Path(__file__).parent)
    data = read_file(os.path.join(base_path, "PuzzleInputFiles", file))
    return data


def read_file(file: str) -> list:
    file_obj = open(file, "r")
    file_data = file_obj.read()
    data = file_data.splitlines()
    file_obj.close()
    return data


def find_number_in_string(s, reverse: bool):
    if reverse:
        s = s[::-1]
    try:
        number = w2n.word_to_num(s)
        if 0 <= number <= 9:
            return number
        else:
            return None
    except ValueError:
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                try:
                    number = w2n.word_to_num(s[i:j])
                    return number
                except ValueError:
                    continue
    return None


def part_2(file):
    num_in_str = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    rev_num_in_str = [element[::-1] for element in num_in_str]
    data = path(file)
    final_numbers = []
    for element in data:
        temp = []
        reverse_temp = []
        characters = list(element)
        ram = ""
        reverse_ram = ""
        for c in characters:
            ram += c
            if any(num in ram for num in num_in_str):
                temp.append(str(find_number_in_string(ram, False)))
                ram = ""
            if str(c).isnumeric():
                ram = ""
                temp.append(str(c))
        for r in reversed(characters):
            reverse_ram += r
            if any(num in reverse_ram for num in rev_num_in_str):
                reverse_temp.append(str(find_number_in_string(reverse_ram, True)))
                reverse_ram = ""
            if str(r).isnumeric():
                reverse_ram = ""
                reverse_temp.append(str(r))
        if len(temp) != 1:
            if reverse_temp[0] != 'None':
                number = temp[0] + reverse_temp[0]
            else:
                number = temp[0] + temp[len(temp) - 1]
        else:
            number = temp[0] + temp[0]
        final_numbers.append(int(number))
    return sum(final_numbers)


def part_1(file):
    data = path(file)
    final_numbers = []
    for element in data:
        temp = []
        characters = list(element)
        for c in characters:
            if str(c).isnumeric():
                temp.append(str(c))
        if len(temp) != 1:
            number = temp[len(temp) - len(temp)] + temp[len(temp) - 1]
        else:
            number = temp[0] + temp[0]
        final_numbers.append(int(number))
    return sum(final_numbers)


if __name__ == '__main__':
    print(f"Part 1:{part_1('part1.txt')}")
    print(f"Part 2:{part_2('part1.txt')}")
