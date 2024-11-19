import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from register import *


def test_username():
	assert validate_username("yosr_nou") == True
	assert validate_username("yosr nou") == False
	assert validate_username("") == False


def test_password():
    assert validate_password("Password1!") == True  
    assert validate_password("short") == False  
    assert validate_password("password") == False  
    assert validate_password("12345678") == False 
    assert validate_password("Password") == False  
    assert validate_password("Password1") == False 

def test_email():
    assert validate_email("test@example.com") == True  
    assert validate_email("test@example") == False  
    assert validate_email("test.com") == False  
    assert validate_email("") == False 