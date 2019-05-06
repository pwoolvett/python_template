def test_import():
    import {{ cookiecutter.slug_name }}

    module = {{ cookiecutter.slug_name }}
    assert module
