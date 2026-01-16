# Main entry point for nuwa_example_lib
# This file compiles into the Python extension module
# Note: The filename determines the Python module name

import nuwa_sdk  # Provides nuwa_export for automatic type stub generation
include helpers  # Include additional modules from nim/ directory

proc greet(name: string): string {.nuwa_export.} =
  ## Greet someone by name
  return make_greeting(name)

proc add(a: int, b: int): int {.nuwa_export.} =
  ## Add two integers together
  return a + b
