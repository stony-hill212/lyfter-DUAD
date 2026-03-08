import pytest
from sum_exercise import calculate_sum,show_sum

def test_calculate_sum_reg():
    assert calculate_sum([1,2,3,4])==10

def test_calculate_sum_empty():
    assert calculate_sum([])==0

def test_calculate_sum_negative_numbers():
    assert calculate_sum([-5,5,-10,10])==0

