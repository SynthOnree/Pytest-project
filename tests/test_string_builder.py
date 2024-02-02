# File: test/test_string_builder.py

# Original class -- adds input string on add method
#onto existing string 

#takes length of string
#returns length

#returns string at the end 

from lib.string_builder import *

"""
Does an empty string output "" and 0
"""

def test_empty_string():
    string_test2 = StringBuilder()
    string_test2.add("")
    assert string_test2.output() == ""


"""
When a string is added
The output method gives that string
"""

def test_check_length_and_return_added_strings():
    string_test = StringBuilder()
    string_test.add("Sausages")
    assert string_test.output() == "Sausages"


"""
When a string is added
The size method gives length
"""

def test_check_length_and_return_added_strings():
    string_test = StringBuilder()
    string_test.add("Sausages")
    assert string_test.size() == 8

"""
When multiple strings are added
The output method gives the strings added as per add method
"""

def test_multiple_strings_output_added():
    string_test = StringBuilder()
    string_test.add("Sausages")
    string_test.add("Eggs")
    string_test.add("Beans")
    assert string_test.output() == "SausagesEggsBeans"

"""
When multiple strings are aded
The size method gives the len of all strings added together
"""

def test_multiple_strings_size_is_added():
    string_test = StringBuilder()
    string_test.add("Sausages")
    string_test.add("Eggs")
    string_test.add("Beans")
    assert string_test.size() == 17
