import pytest
from case_utils import count_cases

def test_count_cases_mixed():
    upper,lower=count_cases("Hello World")
    assert upper==2
    assert lower==8

def test_count_cases_all_upper():
    upper,lower=count_cases("ABCDEF")
    assert upper==6
    assert lower==0

def test_count_cases_no_letters():
    upper,lower=count_cases("1234!@#")
    assert upper==0
    assert lower==0

    