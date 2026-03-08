import pytest
from bubble_sort2 import bubble_sort

def test_small_list():
    data=[5,3,8,4]
    assert bubble_sort(data)==[3,4,5,8]

def test_large_list():
    data=list(range(150,0,-1))
    sorted_data=bubble_sort(data)
    assert sorted_data==sorted(data)

def test_empty_list():
    assert bubble_sort([])==[]

def test_invalid_input():
    with pytest.raises(TypeError):
        bubble_sort("not a list")

    with pytest.raises(TypeError):
        bubble_sort(123)

