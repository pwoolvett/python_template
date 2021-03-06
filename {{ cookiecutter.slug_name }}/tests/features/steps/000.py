from behave import given, when, then

from {{ cookiecutter.slug_name }} import DOTENV_LOCATION


@given("we have behave installed2")
def behave_installed(context):
    pass


@given("this feature2")
def feature_loaded(context):
    pass


@when("we implement a test2")
def sample_assert(context):
    pass


@then("behave will test it for us!2")
def use_context_data(context):
    assert DOTENV_LOCATION
