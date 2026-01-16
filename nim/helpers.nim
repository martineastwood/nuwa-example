# Helper functions for nuwa_example
# These functions are accessible from lib.nim

proc make_greeting(name: string): string =
  ## Create a friendly greeting
  return "Hello, " & name & "!"
