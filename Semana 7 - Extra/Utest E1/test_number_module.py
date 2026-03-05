import pytest
from numbers_module import NumberOperations

num_ops=NumberOperations()

def test_positive_numbers():
    numbers=[10,20,30]
    assert num_ops.sum_numbers(numbers)==60
    assert num_ops.average(numbers)==20
    assert num_ops.celsius_to_fahrenheit(25)==77

def test_negative_numbers():
    numbers=[-10,-20,-30]
    assert num_ops.sum_numbers(numbers)==-60
    assert num_ops.average(numbers)==-20
    assert num_ops.celsius_to_fahrenheit(-10)==14

def test_zero_numbers():
    numbers=[0,0,0]
    assert num_ops.sum_numbers(numbers)==0
    assert num_ops.average(numbers)==0
    assert num_ops.celsius_to_fahrenheit(0)==32
    