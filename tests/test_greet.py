# test greet.py

from lib.greet import *

def test_greet():
    result = greet("Henry")
    assert result == "Hello, Henry!"