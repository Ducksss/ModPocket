"""Tests for helpers module."""

from modpocket_utils.helpers import format_text, chunk_list


def test_format_text():
    """Test the format_text function."""
    assert format_text("  hello  ") == "hello"
    assert format_text("  hello  ", uppercase=True) == "HELLO"
    assert format_text("test") == "test"


def test_chunk_list():
    """Test the chunk_list function."""
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3], 1) == [[1], [2], [3]]
    assert chunk_list([], 2) == []
    assert chunk_list([1, 2, 3, 4], 4) == [[1, 2, 3, 4]]
