import Day1 as sut


def test_part_1():
    r = sut.part_1("testpart1.txt")
    assert r == 142


def test_part_2():
    n = sut.part_2("testpart2.txt")
    assert n == 293
