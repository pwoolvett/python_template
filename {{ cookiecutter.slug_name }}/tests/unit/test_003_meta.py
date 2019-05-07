import pytest


def test_import():
    import {{ cookiecutter.slug_name }}

    meta = {{ cookiecutter.slug_name }}.__meta__
    assert meta


@pytest.mark.parametrize(
    "name",
    [
        ("project_name"),
        ("name"),
        ("version"),
        ("description"),
        ("author"),
        ("maintainer"),
    ],
)
def test_attr(name):
    import {{ cookiecutter.slug_name }}

    meta = {{ cookiecutter.slug_name }}.__meta__
    assert getattr(meta, name)


def test_non_existent():
    from {{ cookiecutter.slug_name }} import __meta__

    with pytest.raises(AttributeError):
        __meta__.asdhjlghksd
