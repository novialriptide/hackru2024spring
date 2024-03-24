from typing import Any
import os
import subprocess
from werkzeug.utils import secure_filename

user_files_directory = "./data/user_files"  # backend/data/user_files
testcases_directory = "./data/testcases"  # backend/data/testcases


def upload_file(username: str, qid: str, file: Any) -> str:
    """
    Create a new file in the user_files directory.

    Args:
        username (str): The username of the user
        qid (str): The question ID
        file (Any): The file object

    Returns:
        None
    """
    filename = secure_filename(f"{username}-{qid}.py")
    path = os.path.join(user_files_directory, filename)
    file.save(path)
    return path


def execute_file(username: str, qid: str) -> str:
    """
    Execute the file uploaded by the user.

    Args:
        username (str): The username of the user
        qid (str): The question ID

    Returns:
        Union[int, str]: The number of test cases passed by the file or an error message
    """
    user_filename = secure_filename(f"{username}-{qid}.py")
    user_path = os.path.join(user_files_directory, user_filename)

    test_filename = f"{qid}.py"
    test_path = os.path.join(testcases_directory, test_filename)

    user_filename = secure_filename(f"{username}-{qid}.py")
    user_path = os.path.join(user_files_directory, user_filename)

    test_filename = f"{qid}.py"
    test_path = os.path.join(testcases_directory, test_filename)

    print(f"Running command: python {test_path} {user_path}")

    try:
        result = subprocess.run(["python", test_path, user_path], capture_output=True)
        if result.returncode != 0:
            stderr_output = result.stderr.decode("utf-8").strip()
            last_line = stderr_output.split("\n")[-1]
            return last_line
        return result.stdout.decode("utf-8").strip()
    except Exception as e:
        return str(e)
