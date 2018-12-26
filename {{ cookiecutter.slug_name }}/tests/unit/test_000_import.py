def test_import():
    import {{ cookiecutter.slug_name }}


    p = {{ cookiecutter.slug_name }}
    assert p
