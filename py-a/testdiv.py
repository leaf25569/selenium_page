import pytest


def div(a, b):
    return a / b


class TestdiV():


    @pytest.mark.happy
    def testdiv(self):
        assert div(6, 2) == 3

    def testdiv1(self):
        assert div(1, -1) == -1

