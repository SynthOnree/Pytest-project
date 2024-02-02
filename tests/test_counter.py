# File: lib/test_counter.py

from lib.counter import *

"""
The original file is a counter, accepting argument for the add method.
"""

"""
Initially, reports a count of zero
"""

def test_counter_initially_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."


"""
When we add a single number to the counter
It is reflected in the final count
"""

def test_increases_count_and_returns_string():
    counter_2 = Counter()
    counter_2.add(5)
    assert counter_2.report() == "Counted to 5 so far."

# So far, we have tested all methods.
    # But not all behaviours / interactions

"""
When we add multiple numbers to the counter
The sum of those numbers if the final count
"""

def test_add_method_twice():
    counter_3 = Counter()
    counter_3.add(5)
    counter_3.add(3)
    counter_3.add(1)
    assert counter_3.report()== "Counted to 9 so far."
