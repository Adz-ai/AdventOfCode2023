import os
from pathlib import Path


def path(file, day):
    data = read_file(get_path(day, file))
    return data


def get_path(day, file):
    base_path = os.path.dirname(Path(__file__).parent)
    return os.path.join(base_path, day, "PuzzleInputFiles", file)


def read_file(file: str) -> list:
    data = open(file, "r").read().splitlines()
    open(file, "r").close()
    return data
