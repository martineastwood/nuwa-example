import nuwa_example

print("Testing nuwa_example...")

# Test basic functionality
result = nuwa_example.greet("World")
print(f"Greeting: {result}")
assert result == "Hello, World!", f"Expected 'Hello, World!', got '{result}'"

# Test addition
sum_result = nuwa_example.add(5, 10)
print(f"5 + 10 = {sum_result}")
assert sum_result == 15, f"Expected 15, got {sum_result}"

print("✅ All tests passed!")
