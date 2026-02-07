"""Tests for example_project"""

import pytest
import numpy as np
from example_project import (
    greet, add, is_even, safe_divide,
    calculate_average, power,
    reverse_string, count_words,
    numpy_array_sum, numpy_array_multiply_scalar
)


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


class TestBooleanReturns:
    """Test functions that return booleans."""

    def test_is_even(self):
        assert is_even(2) == True
        assert is_even(4) == True
        assert is_even(0) == True
        assert is_even(1) == False
        assert is_even(7) == False
        assert is_even(-2) == True


class TestErrorHandling:
    """Test error handling."""

    def test_safe_divide_normal(self):
        assert safe_divide(10.0, 2.0) == 5.0
        assert safe_divide(-10.0, 2.0) == -5.0

    def test_safe_divide_by_zero(self):
        # nimpy raises its own exception type that inherits from Exception
        # The error message confirms "ValueError" is in the exception name
        with pytest.raises(Exception) as exc_info:
            safe_divide(10.0, 0.0)
        assert "ValueError" in str(type(exc_info.value))
        assert "divide by zero" in str(exc_info.value)


class TestCollectionOperations:
    """Test operations on collections."""

    def test_calculate_average(self):
        assert calculate_average([1.0, 2.0, 3.0, 4.0, 5.0]) == 3.0
        assert calculate_average([10.0]) == 10.0
        assert calculate_average([-5.0, 5.0]) == 0.0

    def test_calculate_average_empty(self):
        # nimpy raises its own exception type that inherits from Exception
        # The error message confirms "ValueError" is in the exception name
        with pytest.raises(Exception) as exc_info:
            calculate_average([])
        assert "ValueError" in str(type(exc_info.value))
        assert "empty sequence" in str(exc_info.value)


class TestDefaultParameters:
    """Test functions with default parameters."""

    def test_power_default(self):
        # Default exponent is 2 (square)
        assert power(2.0) == 4.0
        assert power(5.0) == 25.0
        assert power(-3.0) == 9.0

    def test_power_custom_exponent(self):
        assert power(2.0, 10.0) == 1024.0
        assert power(3.0, 3.0) == 27.0
        assert power(10.0, 0.0) == 1.0


class TestStringOperations:
    """Test string manipulation functions."""

    def test_reverse_string(self):
        assert reverse_string("hello") == "olleh"
        assert reverse_string("Python") == "nohtyP"
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"

    def test_count_words(self):
        assert count_words("") == 0
        assert count_words("hello") == 1
        assert count_words("hello world") == 2
        assert count_words("  multiple   spaces  ") == 2


class TestNumPyOperations:
    """Test NumPy array operations."""

    def test_numpy_array_sum(self):
        arr = np.array([1, 2, 3, 4, 5], dtype=np.int64)
        assert numpy_array_sum(arr) == 15

        arr_empty = np.array([], dtype=np.int64)
        assert numpy_array_sum(arr_empty) == 0

        arr_negative = np.array([-1, -2, -3], dtype=np.int64)
        assert numpy_array_sum(arr_negative) == -6

    def test_numpy_array_multiply_scalar(self):
        arr = np.array([1.0, 2.0, 3.0], dtype=np.float64)
        result = numpy_array_multiply_scalar(arr, 2.5)
        assert result == [2.5, 5.0, 7.5]


def test_module_exists():
    """Test that the module can be imported and has expected functions."""
    import example_project

    # Basic functions
    assert hasattr(example_project, 'greet')
    assert hasattr(example_project, 'add')
    assert hasattr(example_project, 'is_even')
    assert hasattr(example_project, 'safe_divide')
    assert callable(example_project.greet)
    assert callable(example_project.add)

    # Collection operations
    assert hasattr(example_project, 'calculate_average')

    # Default parameters
    assert hasattr(example_project, 'power')

    # String functions
    assert hasattr(example_project, 'reverse_string')
    assert hasattr(example_project, 'count_words')

    # NumPy functions
    assert hasattr(example_project, 'numpy_array_sum')
    assert hasattr(example_project, 'numpy_array_multiply_scalar')
