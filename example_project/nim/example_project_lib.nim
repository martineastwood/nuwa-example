# Main entry point for example_project_lib
# This file compiles into the Python extension module
# Note: The filename determines the Python module name

import nuwa_sdk  # Provides nuwa_export for automatic type stub generation
include helpers  # Include additional modules from nim/ directory
import nimpy
import nimpy/raw_buffers
import std/strutils
import std/math

# =============================================================================
# Basic Functions
# =============================================================================

proc greet(name: string): string {.nuwa_export.} =
  ## Greet someone by name
  return make_greeting(name)

proc add(a: int, b: int): int {.nuwa_export.} =
  ## Add two integers together
  return a + b

proc is_even(n: int): bool {.nuwa_export.} =
  ## Check if a number is even
  return n mod 2 == 0

proc safe_divide(a: float, b: float): float {.nuwa_export.} =
  ## Divide two numbers, raise error if dividing by zero
  if b == 0.0:
    raise newException(ValueError, "Cannot divide by zero")
  return a / b

# =============================================================================
# String Operations
# =============================================================================

proc reverse_string(s: string): string {.nuwa_export.} =
  ## Reverse a string
  result = newStringOfCap(s.len)
  for i in countdown(s.high, 0):
    result.add(s[i])

proc count_words(text: string): int {.nuwa_export.} =
  ## Count the number of words in a string
  let words = text.splitWhitespace()
  return words.len

# =============================================================================
# Collection Operations
# =============================================================================

proc calculate_average(numbers: seq[float]): float {.nuwa_export.} =
  ## Calculate the average of a sequence of numbers
  if numbers.len == 0:
    raise newException(ValueError, "Cannot calculate average of empty sequence")
  var sum = 0.0
  for num in numbers:
    sum += num
  return sum / float(numbers.len)

# =============================================================================
# Default Parameters
# =============================================================================

proc power(base: float, exponent: float = 2.0): float {.nuwa_export.} =
  ## Raise base to the given power (defaults to square)
  return pow(base, exponent)

# =============================================================================
# NumPy Array Operations (zero-copy access)
# =============================================================================

proc numpy_array_sum(arr: PyObject): int64 {.nuwa_export.} =
  ## Sum all elements in a numpy array of integers
  ## This works with numpy arrays without copying data
  var buf: RawPyBuffer
  getBuffer(arr, buf, PyBUF_READ or PyBUF_CONTIG_RO)

  let data = cast[ptr UncheckedArray[int64]](buf.buf)
  let size = buf.len div sizeof(int64)

  result = 0
  for i in 0 ..< size:
    result += data[i]

  release(buf)

proc numpy_array_multiply_scalar(arr: PyObject, scalar: float64): seq[float64] {.nuwa_export.} =
  ## Multiply numpy array elements by a scalar and return as Nim sequence
  ## This demonstrates reading from numpy arrays
  var buf: RawPyBuffer
  getBuffer(arr, buf, PyBUF_READ or PyBUF_CONTIG_RO)

  let data = cast[ptr UncheckedArray[float64]](buf.buf)
  let size = buf.len div sizeof(float64)

  result = newSeq[float64](size)
  for i in 0 ..< size:
    result[i] = data[i] * scalar

  release(buf)
