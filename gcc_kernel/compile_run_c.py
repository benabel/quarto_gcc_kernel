import subprocess
from shlex import split
import os


def compile_run_c(c_code):
    try:
        # Step 1: Compile the C code from the string
        compile_command = split("gcc -x c -o test_code -")
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
