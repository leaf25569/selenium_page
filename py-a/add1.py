import pytest


def addmarh(b):
    a = 1 + b
    return a

def test_addmarcha():
    assert addmarh(3) == 4


class Testmath1:
    @pytest.mark.happy
    def test_one(self):
        assert addmarh(3) == 4



