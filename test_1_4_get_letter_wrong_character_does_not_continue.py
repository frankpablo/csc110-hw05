import pytest
import hw05
from unittest.mock import patch



# Globals
st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]


# Part 1
# ===========
def test_1_4_get_letter_wrong_character_does_not_continue(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["@", "F", "A"]) as mock_input:
        result = hw05.get_letter()
    hint2 = f"\n\n *** Did your loop break after a successful symbol was provided? \n *** Did it continue if the word was wrong?"
    assert mock_input.call_count == 3, hint2

