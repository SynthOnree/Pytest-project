# File: tests/test_gratitude.py
from lib.gratitudes import *

"""
test 2 add methods format as expected
"""

def test_name():
    gratitude1 = Gratitudes()
    gratitude1.add("Kiwi fruit")
    gratitude1.add("Parrots")
    assert gratitude1.format() == "Be grateful for: Kiwi fruit, Parrots"

"""
test gratitudes is a list
"""

def test_name_2():
    gratitude2 = Gratitudes()
    assert gratitude2.gratitudes == []
