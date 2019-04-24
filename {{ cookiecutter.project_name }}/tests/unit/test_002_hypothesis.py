from hypothesis import given
from hypothesis.strategies import floats

EPSILON = 0.0001


@given(floats().filter(lambda x: x >= 0))
def test_hypothesis_sqrt_all(num):
    assert abs(num - ((num ** 2) ** 0.5) ) < EPSILON

@given(floats())
def test_hypothesis_sqrt_all(num):
    assert abs(num - ((num ** 2) ** 0.5) ) < EPSILON
