"""Tests for nuwa_example"""

import pytest
from nuwa_example import greet, add


class TestGreet:
    """Test the greet function."""

    def test_greet_world(self):
        assert greet("World") == "Hello, World!"

    def test_greet_empty(self):
        assert greet("") == "Hello, !"

    def test_greet_unicode(self):
        assert greet("🐍") == "Hello, 🐍!"


class TestAdd:
    """Test the add function."""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, 1) == 0
        assert add(-5, -3) == -8

    def test_add_zero(self):
        assert add(0, 0) == 0
        assert add(5, 0) == 5


def test_module_exists():
    """Test that the module can be imported and has expected functions."""
    import nuwa_example

    assert hasattr(nuwa_example, 'greet')
    assert hasattr(nuwa_example, 'add')
    assert callable(nuwa_example.greet)
    assert callable(nuwa_example.add)
