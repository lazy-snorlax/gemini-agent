import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = abs_working_dir

    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    
    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(['python', target_file], capture_output=True, timeout=30, text=True, cwd=abs_working_dir)
        if result.stdout == "" and result.stderr == "":
            stdout = "No output produced"
            stderr = "No output produced"
        else:
            stdout = f'STDOUT: {result.stdout}'
            stderr = f'STDERR: {result.stderr}'

        if result.returncode == 0:
            return f"{stdout} \n {stderr}"

        return f"Process exited with code {result.returncode} \n {stdout} \n {stderr}"

    except Exception as e:
        return f'Error: executing Python file: {e}'