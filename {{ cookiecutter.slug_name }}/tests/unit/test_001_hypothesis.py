import pytest
from hypothesis import given
from hypothesis.strategies import floats

EPSILON = 0.0001

ANY_FLOATS = floats()
SAFE_FLOATS = floats(
    min_value=0,
    allow_infinity=False,
    allow_nan=False,
    max_value=1.34e+154
)


@pytest.mark.xfail
@given(ANY_FLOATS)
def test_hypothesis_sqrt_all(num):
    assert abs(num - ((num ** 2) ** 0.5)) < EPSILON


@given(SAFE_FLOATS)
def test_hypothesis_sqrt_non_negative(num):
    assert abs(num - ((num ** 2) ** 0.5)) < EPSILON
