import pytest
from main import round6


def test_round6_rounds_up():
  assert round6(9.7) == 10


def test_round6_rounds_down():
  assert round6(8.5) == 8

pytest.main()