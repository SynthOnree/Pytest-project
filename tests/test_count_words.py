# File: tests/test_count_words.py

# A function called count_words that takes a string as 
# an argument and returns the number of words in that string.

import pytest
from lib.count_words import *

"""
Function takes a string
Returns string
"""

# def test_input_string_return_string():
#     result = count_words("test string")
#     assert result == "test string"

"""
Function counts words in string
returns count
"""

def test_return_count_of_string():
    result = count_words("test string")
    assert result == 2