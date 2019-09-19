import pytest


@pytest.mark.smoke
def test_one():
    assert True


@pytest.mark.regression
def test_two():
    assert True


@pytest.mark.kek
def test_three():
    assert True
