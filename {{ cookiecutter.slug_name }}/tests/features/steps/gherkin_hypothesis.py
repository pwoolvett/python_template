from behave import given, when, then
from hypothesis import given as generate
from hypothesis.strategies import floats

# TODO: import package modules here

SAFE_FLOATS = floats(
    min_value=0, allow_infinity=False, allow_nan=False, max_value=1.34e154
)


@given("we have a float number")
@generate(SAFE_FLOATS)
def generate_float(context, flt):
    context.number = flt


@when("we square it")
def square_float(context):
    context.result = context.number ** 2


@when("we take the root")
def root_float(context):
    context.result = context.result ** 0.5


@then("the result equals the original argument")
def compar_input_output(context):
    assert context.result == context.number, f"{context.number}"
