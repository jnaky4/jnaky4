import pytest


def test_subtract_score(*points):
    outof10 = 10
    for score in points:
        outof10 -= score
    assert outof10 >= 0
    return outof10


test_subtract_score(2, 3, 4)
