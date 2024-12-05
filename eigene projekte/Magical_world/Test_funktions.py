import pytest
import main_magical_world as pm



def test_list_sclicing():
  a = ["2, 4, 8%"]

  assert pm.display_all_results(a) == "2, 4, 8%"
