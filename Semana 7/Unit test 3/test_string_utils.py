import pytest
from string_utils import flip_string

def test_flip_string_normal():
    assert flip_string("hello")=="olleh"

def test_flip_string_empty():
    assert flip_string("")==""

def test_flip_string_with_spaces():
    assert flip_string("Greco Roman")=="namoR ocerG"

