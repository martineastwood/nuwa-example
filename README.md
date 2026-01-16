# nuwa-example

A Nim extension for Python built with [Nuwa Build](https://github.com/martineastwood/nuwa-build).

## Features

- ✅ **Zero-configuration** build system
- ✅ **Automatic type stubs** (`.pyi` files) for IDE autocomplete
- ✅ **Fast Nim compilation** with easy Python integration
- ✅ **Editable installs** for rapid development
- ✅ **GitHub Actions** workflow for automated PyPI publishing

## Installation

```bash
pip install .
```

## Development

```bash
# Compile debug build (generates .so and .pyi files)
nuwa develop

# Compile release build (optimized)
nuwa develop --release

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
nuwa-example/
├── .github/
│   └── workflows/
│       └── publish.yml          # PyPI/PyCI publishing workflow
├── nim/                          # Nim source files
│   ├── nuwa_example_lib.nim    # Main entry point (filename = module name)
│   └── helpers.nim              # Additional modules
├── nuwa_example/               # Python package
│   ├── __init__.py              # Package wrapper (can add Python code here)
│   ├── nuwa_example_lib.so     # Compiled Nim extension (generated)
│   └── nuwa_example_lib.pyi    # Type stubs (generated)
├── tests/                       # Test files
│   └── test_nuwa_example.py    # Pytest tests
├── example.py                   # Example usage
└── pyproject.toml               # Project configuration
```

The compiled extension is named `nuwa_example_lib.so` to avoid conflicts with the
Python package. Your `__init__.py` imports from it and can add Python wrappers.

## Usage

```python
import nuwa_example

# Call Nim-compiled functions (with full IDE support!)
result = nuwa_example.greet("World")
print(result)  # "Hello, World!"

sum_result = nuwa_example.add(5, 10)
print(sum_result)  # 15
```

## Adding New Functions

1. Edit `nim/nuwa_example_lib.nim`:
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
from nuwa_example import my_function

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
pytest tests/test_nuwa_example.py::test_greet_world
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
     - PyPI Project Name: `nuwa-example`
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
- Support Python 3.9, 3.10, 3.11, 3.12, and 3.13
- Build a source distribution
- Publish everything to PyPI
