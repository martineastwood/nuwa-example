"""
example_project - A Nim extension for Python

This package wraps the compiled Nim extension and provides Python-level functionality.

You can import Nim functions directly from the compiled extension, or wrap them
with Python code for additional processing.
"""

# Import the compiled Nim extension functions
# Note: Star imports don't work reliably with extension modules,
# so we explicitly import the functions we want to expose
from .example_project_lib import (
    # Basic functions
    add, greet, is_even, safe_divide,
    # Collection operations
    calculate_average,
    # Default parameters
    power,
    # String operations
    reverse_string, count_words,
    # NumPy operations
    numpy_array_sum, numpy_array_multiply_scalar,
)

__version__ = "0.1.0"
