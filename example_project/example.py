import example_project
import numpy as np

print("=" * 60)
print("Testing example_project")
print("=" * 60)

# =============================================================================
# Basic Functions
# =============================================================================

print("\n### Basic Functions ###")

result = example_project.greet("World")
print(f"greet('World') = '{result}'")
assert result == "Hello, World!"

sum_result = example_project.add(5, 10)
print(f"add(5, 10) = {sum_result}")
assert sum_result == 15

print(f"is_even(4) = {example_project.is_even(4)}")
print(f"is_even(7) = {example_project.is_even(7)}")

print(f"safe_divide(10.0, 2.0) = {example_project.safe_divide(10.0, 2.0)}")
try:
    example_project.safe_divide(10.0, 0.0)
except Exception as e:
    print(f"safe_divide(10.0, 0.0) raises: {type(e).__name__}: {e}")

# =============================================================================
# Collection Operations
# =============================================================================

print("\n### Collection Operations ###")

avg = example_project.calculate_average([1.0, 2.0, 3.0, 4.0, 5.0])
print(f"calculate_average([1.0, 2.0, 3.0, 4.0, 5.0]) = {avg}")
assert avg == 3.0

# =============================================================================
# Default Parameters
# =============================================================================

print("\n### Default Parameters ###")

print(f"power(3.0) = {example_project.power(3.0)}")  # defaults to square
print(f"power(2.0, 10.0) = {example_project.power(2.0, 10.0)}")

# =============================================================================
# String Operations
# =============================================================================

print("\n### String Operations ###")

reversed_str = example_project.reverse_string("Hello World")
print(f"reverse_string('Hello World') = '{reversed_str}'")
assert reversed_str == "dlroW olleH"

word_count = example_project.count_words("The quick brown fox jumps over the lazy dog")
print(f"count_words('The quick brown fox...') = {word_count}")
assert word_count == 9

# =============================================================================
# NumPy Array Operations
# =============================================================================

print("\n### NumPy Array Operations ###")

# Sum array elements (zero-copy access)
arr = np.array([1, 2, 3, 4, 5], dtype=np.int64)
arr_sum = example_project.numpy_array_sum(arr)
print(f"numpy_array_sum(np.array([1,2,3,4,5])) = {arr_sum}")
assert arr_sum == 15

# Read numpy array, process in Nim, return as list
arr_float = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)
multiplied = example_project.numpy_array_multiply_scalar(arr_float, 2.5)
print(f"numpy_array_multiply_scalar([1.0,2.0,3.0,4.0,5.0], 2.5) = {multiplied}")
assert multiplied == [2.5, 5.0, 7.5, 10.0, 12.5]

print("\n" + "=" * 60)
print("✅ All tests passed!")
print("=" * 60)
