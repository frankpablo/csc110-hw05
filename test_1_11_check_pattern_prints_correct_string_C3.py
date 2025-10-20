import pytest
import hw05
from unittest.mock import patch



# Globals
st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]


# Part 3
# ===========

def test_1_11_check_pattern_prints_correct_string_C3(capsys, monkeypatch):
    let = "C"
    dig = "3"
    result = hw05.check_pattern(let, dig, st_list)
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    printout = printout.strip("\n")
    expected = "Strings with the pattern:\n<Nothing>"
    len_p = len(printout)
    len_exp = len("Strings with the pattern:")
    hint1 = f"\n\n *** For input \n{let+dig}\n *** Your printout after \'Strings with the pattern:\' should be an empty line.\n\n"
    msg1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}\n\n"
    # msg2 = f"the length of the expected 'Strings with the pattern:' is {len_exp}\n\n"
    # msg3 = f"the length of the printed 'Strings with the pattern:' is {len_p}\n"
    msg = hint1+msg1
    cond =  len_exp-2  < len_p < len_exp+2
    assert cond, msg

