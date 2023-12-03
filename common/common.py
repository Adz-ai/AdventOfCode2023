import os
from pathlib import Path


def path(file, day):
    base_path = os.path.dirname(Path(__file__).parent)
    data = read_file(os.path.join(base_path, day,"PuzzleInputFiles", file))
    return data


def read_file(file: str) -> list:
    data = open(file, "r").read().splitlines()
    open(file, "r").close()
    return data
