import pytest
import time

@pytest.mark.incremental
class TestUserHandling:
    def test_login(self):
        print("This will execute first")
        assert True

    def test_modification(self):
        print("This will execute second, and fail")
        assert False

    def test_deletion(self):
        print("This will not excecute, since test_modification fails")
        assert False


def test_true():
    assert True

def test_false():
    assert False
