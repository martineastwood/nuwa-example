# example_project

A Nim extension for Python built with [Nuwa Build](https://github.com/martineastwood/nuwa-build).

## Features

- ✅ **Zero-configuration** build system
- ✅ **Automatic type stubs** (`.pyi` files) for IDE autocomplete
- ✅ **Fast Nim compilation** with easy Python integration
- ✅ **Build profiles** for debug, release, and benchmarking
- ✅ **Editable installs** for rapid development
- ✅ **GitHub Actions** workflow for automated PyPI publishing

## Installation

```bash
pip install .
```

## Development

```bash
# Compile debug build (generates compiled extension and .pyi files)
nuwa develop

# Use build profiles for different scenarios
nuwa develop --profile dev      # Debug build with symbols
nuwa develop --profile release  # Optimized release build
nuwa develop --profile bench    # Optimized with stack traces for profiling

# Run example
python example.py

# Run tests (requires pytest)
pip install pytest
pytest
```

## Type Stubs

This project automatically generates Python type stubs (`.pyi` files) during compilation. This means:

- ✨ **IDE autocomplete**: Your editor shows exact function signatures
- 🔍 **Type checking**: `mypy` and `pyright` can check your code
- 📖 **Documentation**: Docstrings appear in hover tooltips

Example type stub for `add`:
```python
def add(a: int, b: int) -> int:
    """Add two integers together"""
    ...
```

## Project Structure

```
example_project/
├── .github/
│   └── workflows/
│       └── publish.yml          # PyPI/PyCI publishing workflow
├── nim/                          # Nim source files
│   ├── example_project_lib.nim    # Main entry point (filename = module name)
│   └── helpers.nim              # Additional modules
├── example_project/               # Python package
│   ├── __init__.py              # Package wrapper (can add Python code here)
│   ├── example_project_lib.<ext>  # Compiled Nim extension (platform-specific, generated)
│   └── example_project_lib.pyi    # Type stubs (generated)
├── tests/                       # Test files
│   └── test_example_project.py    # Pytest tests
├── example.py                   # Example usage
└── pyproject.toml               # Project configuration
```

The compiled extension is named `example_project_lib.<ext>` where `<ext>` is the
platform-specific extension (e.g., `.so`, `.pyd`, or `.cpython-310-x86_64-linux-gnu.so`).
This avoids conflicts with the Python package. Your `__init__.py` imports from it
and can add Python wrappers.

## Usage

```python
import example_project
import numpy as np

# Basic operations (with full IDE support!)
result = example_project.greet("World")
print(result)  # "Hello, World!"

sum_result = example_project.add(5, 10)
print(sum_result)  # 15

# Boolean returns
print(example_project.is_even(4))  # True
print(example_project.is_even(7))  # False

# Error handling
print(example_project.safe_divide(10.0, 2.0))  # 5.0
# example_project.safe_divide(10.0, 0.0)  # Raises ValueError

# Collection operations
avg = example_project.calculate_average([1.0, 2.0, 3.0, 4.0, 5.0])
print(avg)  # 3.0

# Default parameters
print(example_project.power(3.0))  # 9.0 (defaults to square)
print(example_project.power(2.0, 10.0))  # 1024.0

# String operations
example_project.reverse_string("hello")  # "olleh"
example_project.count_words("hello world")  # 2

# NumPy array operations (zero-copy access)
arr = np.array([1, 2, 3, 4, 5], dtype=np.int64)
example_project.numpy_array_sum(arr)  # 15

arr_float = np.array([1.0, 2.0, 3.0], dtype=np.float64)
example_project.numpy_array_multiply_scalar(arr_float, 2.5)  # [2.5, 5.0, 7.5]
```

### Example Functions

This project demonstrates common patterns for Nim-Python interop:

#### Basic Types
- `greet(name: string)` - String in, string out
- `add(a: int, b: int)` - Multiple parameters, primitive types
- `is_even(n: int)` - Boolean return type

#### Error Handling
- `safe_divide(a: float, b: float)` - Raises exceptions for invalid input

#### Collections
- `calculate_average(numbers: seq[float])` - Process sequences, return float

#### Default Parameters
- `power(base: float, exponent: float = 2.0)` - Optional parameter with default

#### String Operations
- `reverse_string(s: string)` - String manipulation in Nim
- `count_words(text: string)` - Using Nim's stdlib

#### NumPy Arrays (zero-copy)
- `numpy_array_sum(arr)` - Read int64 arrays, return scalar
- `numpy_array_multiply_scalar(arr, scalar)` - Read float64 arrays, return list

## Adding New Functions

1. Edit `nim/example_project_lib.nim`:
```nim
import nuwa_sdk

proc my_function(x: int, y: int): string {.nuwa_export.} =
  ## Your function documentation
  return "Result: " & $(x + y)
```

2. Recompile:
```bash
nuwa develop
```

3. Use from Python (with full autocomplete):
```python
from example_project import my_function

# Your IDE shows: my_function(x: int, y: int) -> str
result = my_function(5, 10)
```

## Testing

The project includes pytest tests for the Nim extension:

```bash
# Install test dependencies
pip install pytest

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_example_project.py::test_greet_world
```

## Publishing to PyPI

This project includes a GitHub Actions workflow (`.github/workflows/publish.yml`) that automatically builds and publishes wheels to PyPI when you push a version tag:

```bash
git tag v1.0.0
git push origin v1.0.0
```

The workflow uses [cibuildwheel](https://github.com/pypa/cibuildwheel) to build wheels across multiple platforms (Linux, macOS, Windows) and Python versions, then publishes them to PyPI using [Trusted Publishing](https://docs.pypi.org/trusted-publishers/).

### First-time Setup

1. **Configure Trusted Publishing** on PyPI:
   - Go to https://pypi.org/manage/account/publishing/
   - Add a new publisher with:
     - PyPI Project Name: `example_project`
     - Owner: Your GitHub username/organization
     - Repository name: Your repository name
     - Workflow name: `publish.yml`

2. **Push a tag** to trigger the workflow:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

The workflow will automatically:
- Build wheels for Linux, macOS, and Windows
- Support Python 3.9, 3.10, 3.11, 3.12, 3.13, 3.14
- Build a source distribution
- Publish everything to PyPI
