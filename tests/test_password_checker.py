# File: tests/test_password_checker.py

import pytest
from lib.password_checker import *

"""
If password us equal to 8 characters
return True
"""
def test_password_equal_to_8():
    test_password = PasswordChecker()
    assert test_password.check("12345678") == True

"""
If password is greater than 8 characters
return True
"""
def test_password_greater_than_8():
    test_password = PasswordChecker()
    assert test_password.check("1234567890") == True

"""
If password is fewer than 8 characters
Expcetion raises with error message 'invalid password...'
"""

def test_password_fewer_than_8():
    test_password = PasswordChecker()
    with pytest.raises(Exception) as e:
        test_password.check("12345")
    error_message = str(e.value)
    assert error_message == ("Invalid password, must be 8+ characters.")