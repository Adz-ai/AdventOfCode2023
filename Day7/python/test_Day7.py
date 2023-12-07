import Day7 as sut


def test_part_1():
    r = sut.part_1("testpart1.txt")
    assert r == 6440


def test_part_2():
    r = sut.part_2("testpart1.txt")
    assert r == 5905
