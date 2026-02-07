# Stubs for example_project_lib
from typing import Any, List

def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a sequence of numbers"""
    ...

def safe_divide(a: float, b: float) -> float:
    """Divide two numbers, raise error if dividing by zero"""
    ...

def add(a: int, b: int) -> int:
    """Add two integers together"""
    ...

def power(base: float, exponent: float = ...) -> float:
    """Raise base to the given power (defaults to square)"""
    ...

def numpy_array_sum(arr: Any) -> int:
    """
    Sum all elements in a numpy array of integers
    This works with numpy arrays without copying data
    """
    ...

def is_even(n: int) -> bool:
    """Check if a number is even"""
    ...

def reverse_string(s: str) -> str:
    """Reverse a string"""
    ...

def greet(name: str) -> str:
    """Greet someone by name"""
    ...

def count_words(text: str) -> int:
    """Count the number of words in a string"""
    ...

def numpy_array_multiply_scalar(arr: Any, scalar: float) -> list[float]:
    """
    Multiply numpy array elements by a scalar and return as Nim sequence
    This demonstrates reading from numpy arrays
    """
    ...
