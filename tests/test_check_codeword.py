# File: tests/test_check_codework.py

from lib.check_codeword import check_codeword

"""
If the codeword is correct
Returns "Correct! Come in."
"""

def test_check_codework_returns_correct():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

"""
If the codework has the incorrect first & last letter
"""
def test_check_codework_returns_incorrect():
    result = check_codeword('sheep')
    assert result == "WRONG!"

"""
If the codeword has the correct first letter
 and last letter
"""
def test_check_codework_returns_close():
    result = check_codeword('horee')
    assert result == "Close, but nope."

"""
If the codeword has the incorrect first letter 
but correct last letter
"""
def test_with_wrong_first_letter():
    result = check_codeword('aorse')
    assert result == "WRONG!"

"""
If the codeword has the correct first letter
 but incorrect last letter
"""
def test_with_wrong_last_letter():
    result = check_codeword('horsr')
    assert result == "WRONG!"