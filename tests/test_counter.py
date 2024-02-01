# File: lib/test_counter.py

from lib.counter import *

"""
The original file is a counter, accepting argument for the add method.
"""


"""
Test giving add method 5
"""

def test_increases_count_and_returns_string():
    counter_2 = Counter()
    counter_2.add(5)
    result = counter_2.report()
    assert result == "Counted to 5 so far."

"""
if class can work through two uses of add method
"""

