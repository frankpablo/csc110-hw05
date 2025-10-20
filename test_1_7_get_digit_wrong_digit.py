import pytest
import hw05
from unittest.mock import patch



# Globals
st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]


# Part 2
# ===========
def test_1_7_get_digit_wrong_digit(capsys, monkeypatch):
    with patch('builtins.input', side_effect=["@", "1"]) as mock_input:
        result = hw05.get_digit()
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "Error: your input should be only digits."
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1
