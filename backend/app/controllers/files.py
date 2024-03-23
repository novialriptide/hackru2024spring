from typing import Any
import os
from werkzeug.utils import secure_filename


def upload_file(username: str, qid: str, file: Any) -> None:
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
    directory = "./data/user_files"
    full_path = os.path.join(directory, filename)
    file.save(full_path)
