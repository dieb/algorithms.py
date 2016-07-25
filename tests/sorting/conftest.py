import pytest


@pytest.fixture
def assert_sorted():
    def assert_fun(original, sort_function):
        assert sorted(original[:]) == sort_function(original[:])
    return assert_fun
