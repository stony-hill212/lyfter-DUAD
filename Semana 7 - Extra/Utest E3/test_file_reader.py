import pytest
from unittest.mock import mock_open,patch
from file_reader import read_lines

def test_read_lines_success():
    fake_file_content="line1\nline2\nline3\n"
    with patch("builtins.open", mock_open(read_data=fake_file_content)):
        result=read_lines("fake_path.txt")
    assert result==["line1\n", "line2\n", "line3\n"]

def test_read_lines_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError, match="File not found"):
            read_lines("missing_file.txt")