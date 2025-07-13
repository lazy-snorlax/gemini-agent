import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = abs_working_dir

    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{target_file}"'
    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            return f'{file_content_string} [...File "{target_file}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f"Error: {e}"
    