import pytest
from dash_sort_utils import sort_dashed_str

def test_sort_dashed_str_normal():
    result=sort_dashed_str("kick-Punch-shoot")
    assert result=="kick-Punch-shoot"

def test_sort_dashed_str_sorted():
    result=sort_dashed_str("Punch-kick-shoot")
    assert result=="kick-Punch-shoot"

def test_sort_dashed_str_single_word():
    result=sort_dashed_str("kick")
    assert result=="kick"

def test_sort_dashed_str_invalid_type():
    with pytest.raises(TypeError):
        sort_dashed_str(123)

