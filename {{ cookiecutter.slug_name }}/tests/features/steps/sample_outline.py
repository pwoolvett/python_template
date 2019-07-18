from behave import given, when, then
from collections import defaultdict

@given("a set of specific users")
def behave_installed(context):

    context.dep2name = defaultdict(list)

    for row in context.table:
        context.dep2name[row["department"]].append(row["name"])


@when("we count the number of people in each department")
def feature_loaded(context):
    context.counts = {
        dep: len(names)
        for dep, names in context.dep2name.items()
    }


@then("we will find {count} people in {department}")
def use_context_data(context, count, department):
    assert context.counts[department] == int(count)
