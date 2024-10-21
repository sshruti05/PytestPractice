import math
import pytest

@pytest.mark.parametrize('test_input',[82,78,90, 66])
def test_param01(test_input):
    print("start")
    assert test_input < 95
    print("end")

@pytest.mark.parametrize('inp, out', [(2, 4), (3,27), (4, 256)])
def test_param02(inp, out):
    assert (inp ** inp) == out

data = [
    ([2,3,4], 'sum', 9),
    ([2,3,4], 'prod', 24),
]

@pytest.mark.parametrize("a, b, c", data)
def test_param03(a, b, c):
    if b == 'sum':
        assert sum(a) == c
    elif b == 'prod':
        assert math.prod(a) == c

