# File: test_TDD_test.py

# A function called make_snippet that takes a string as an
#  argument and returns the first five words and 
# then a '...' if there are more than that.

import pytest
from lib.TDD_test import *

"""
Function intent:
take string input
return the first five words and then a ... if more than 5 words inputted
"""

"""
Given an emptuy string,
return empty string
"""

def test_empty_string_return_empty_string():
    result = make_snippet("")
    assert result == ""

"""
Given a string of 4, return string of 4
"""

def test_return_string():
    result = make_snippet("I like to party")
    assert result == "I like to party"

"""
Given a string of 5, return string of 5
"""

def test_return_5():
    result = make_snippet("I like to party like")
    assert result == "I like to party like"

"""
Given string 7 words, return 5, add a ... to the end
"""

def test_return_ellipsis_if_more_than_5_in_string():
    result = make_snippet("I like to party like Andrew WK")
    assert result == "I like to party like..."

"""
If string equals 5
don't add ellipsis
"""

def test_no_ellipsis_for_5_words():
    result = make_snippet("I like to party like")
    assert result == "I like to party like"

"""
If given string of 8 words delimted by commas
return first 5 words with ellipsis
"""

def test_8_words_with_commas():
    result = make_snippet("I, like, to, party, like, Andrew, WK")
    assert result == "I like to party like..."