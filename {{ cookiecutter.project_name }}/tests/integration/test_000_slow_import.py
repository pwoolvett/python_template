import pytest
import time

@pytest.mark.slow
def test_slow_import():
    import {{ cookiecutter.slug_name }}

    print('Performing expensive task...')
    time.sleep(10)

    p = {{ cookiecutter.slug_name }}
    assert p
