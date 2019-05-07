def test_import():
    import {{ cookiecutter.slug_name }}

    module = {{ cookiecutter.slug_name }}
    assert module

def test_run(monkeypatch):
    import imp
    import sys
    with monkeypatch.context() as patcher:
        patcher.setattr(sys, 'argv',[''])
        imp.load_source('__main__', '{{ cookiecutter.slug_name }}/__main__.py')
