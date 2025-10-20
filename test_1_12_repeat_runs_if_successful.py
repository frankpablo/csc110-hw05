import pytest
import hw05
from unittest.mock import patch



# Globals
st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]



# Part 4
# ===========
def test_1_12_repeat_runs_if_successful(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["C", "2", "y", "A", "1", "n", "C"]) as mock_input:
        result = hw05.main()
    hint = "\n\n**** DEBUGGING HINT: \n you should restart the main loop if the input is 'y' and stop it otherwise"
    assert mock_input.call_count == 6, hint


