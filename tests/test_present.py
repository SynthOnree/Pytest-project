# File: tests/test_present.py


import pytest
from lib.present import *


"""
Contents has value
Unwrap method doesn't raise Exception
"""
def test_present_unwrap_contents_full():
    present = Present()
    present.wrap("Saxophone")
    present.unwrap()
    assert present.unwrap() == "Saxophone"

"""
contents is None
unwrap method raises Exception
"""

def test_present_unwrap_contents_none():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == ("No contents have been wrapped.")


"""
Contents has value
wrap method raises exception
"""    
def test_present_wrap_contents_has_value():
    present = Present()
    present.wrap("Saxophone")
    with pytest.raises(Exception) as e:
        present.wrap("Trumpet")
    error_message = str(e.value)
    assert error_message == ("A contents has already been wrapped.")

"""
If we wrap an already wrapped present
Wrap method doesn't overwrite - original is preserved
"""
def test_wrapping_twice_does_not_overwrite():
    present = Present()
    present.wrap("Saxophone")
    with pytest.raises(Exception) as e:
        present.wrap("Trumpet")
    assert present.unwrap() == "Saxophone"

# """
# Contents is None
# wrap method raises exception
# """    
# def test_present_wrap_contents_none():
#     present = Present()
#     with pytest.raises(Exception) as e:
#         present.wrap()
#     error_message = str(e.value)
#     assert error_message == ("No contents have been wrapped.")







    



