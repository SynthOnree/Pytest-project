# File test_report_length.py

from lib.report_length import report_length

"""
If function calculates len correctly
"""

def test_len_returns_correct():
    result = len('sausage')
    assert result == 7

"""
If function returns formatted string
"""
def test_function_returns_formatted_string():
    result = report_length('sausages')
    assert result == "This string was 8 characters long."