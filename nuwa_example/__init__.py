"""
nuwa_example - A Nim extension for Python

This package wraps the compiled Nim extension and provides Python-level functionality.

You can import Nim functions directly from the compiled extension, or wrap them
with Python code for additional processing.
"""

# Import the compiled Nim extension functions
# Note: Star imports don't work reliably with extension modules,
# so we explicitly import the functions we want to expose
from .nuwa_example_lib import add, greet

__version__ = "0.1.0"

# Example: Wrap Nim functions with Python code
# def validate_dataframe(df, column_name):
#     '''Example: Extract data from pandas DataFrame and validate with Nim'''
#     import numpy as np
#     from ctypes import c_void_p
#
#     # Extract data as numpy array (zero-copy view)
#     data = df[column_name].to_numpy()
#
#     # Get pointer and pass to Nim for validation
#     from . import nuwa_example_lib
#     result = nuwa_example_lib.validate_array(
#         data.ctypes.data_as(c_void_p),
#         len(data)
#     )
#     return result
