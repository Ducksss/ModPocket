"""Tests for example module."""

from modpocket_core.example import greet, calculate_sum


def test_greet():
    """Test the greet function."""
    result = greet("World")
    assert result == "Hello, World! Welcome to ModPocket Core."
    assert isinstance(result, str)


def test_calculate_sum():
    """Test the calculate_sum function."""
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(0, 0) == 0
    assert calculate_sum(-1, 1) == 0
    assert calculate_sum(100, 200) == 300
