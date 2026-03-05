import pytest
from calculator import divide

def test_divide_valid():
    result=divide(10,2)
    assert result==5.0

def test_divide_by_zero():
    with pytest.raises(ValueError,match="Cannot divide by 0"):
        divide(10,0)

def test_divide_string():
    with pytest.raises(TypeError):
        divide("10",2)