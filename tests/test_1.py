import pytest


@pytest.mark.filterwarnings
@pytest.mark.slow
def test_example():
    assert 1 == 1
