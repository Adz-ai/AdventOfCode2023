import Day6 as sut


def test_part_1():
    r = sut.part_1("testpart1.txt")
    assert r == 288


def test_part_2():
    r = sut.part_2("testpart1.txt")
    assert r == 71503
