from app.extensions import login_manager
from flask import current_app
from werkzeug.security import generate_password_hash
from typing import Dict, Any

def user_exists(username: str) -> bool:
    """
    Check if a user exists in the "users" table

    Args:
        username (str): The username of the user

    Returns:
        bool: True if the user exists, False otherwise
    """
    return get_user(username) is not None

def get_user(username: str) -> Dict[str, str]:
    """
    Get a user from the "users" table

    Args:
        username (str): The username of the user

    Returns:
        Dict[str, str]: The user
    """
    return current_app.db.users.find_one({"username": username})

def create_user(username: str, password: str) -> Dict[str, Any]:
    """
    Create a new user in the "users" table

    Args:
        username (str): The username of the user
        password (str): The password of the user

    Returns:
        Dict[str, Any]: The user
    """
    new_user = {
        "username": username,
        "password": generate_password_hash(
            password, method="pbkdf2:sha256:100", salt_length=8
        ),
    }

    current_app.db.users.insert_one(new_user)
    return new_user

def delete_user(username: str) -> None:
    """
    Delete a user from the "users" table

    Args:
        username (str): The username of the user
    """
    user = get_user(username)
    if user:
        current_app.db.users.delete_one({"username": username})
    