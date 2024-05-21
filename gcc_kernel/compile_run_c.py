import subprocess
from shlex import split
import os
import ast

def has_main_function(c_code):
  """Checks if a text string c_code defines a main function.

  Args:
    c_code: A string containing C code.

  Returns:
    True if a main function is found, False otherwise.
  """
  try:
    tree = ast.parse(c_code)
  except SyntaxError:
    return False

  # Look for FunctionDef nodes with name 'main'
  for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == "main":
      return True
  return False

def compile_run_c(c_code):
    if not has_main_function(c_code):
        c_code = f"""#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main() {{
{c_code}
return 0;
}}"""

    try:
        # Step 1: Compile the C code from the string
        compile_command = split("gcc -std=c99 -x c -o test_code -")
        compile_process = subprocess.run(compile_command, input=c_code, encoding="utf-8", check=True, capture_output=True)
        print("Compilation output:", compile_process.stdout)
        print("Compilation errors:", compile_process.stderr)

        # Step 2: Run the compiled executable
        run_command = ["./test_code"]
        run_process = subprocess.run(run_command, check=True, capture_output=True, text=True)
        print("Program output:", run_process.stdout)

        # Clean up: Remove the compiled executable

        os.remove("test_code")
        return run_process.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}\n{e.stderr}"
