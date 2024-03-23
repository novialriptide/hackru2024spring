from flask_login import UserMixin
from typing import Dict
from flask import current_app
from app.extensions import login_manager

class User(UserMixin):
    """
    Represents a user in the system. Each instance of a user is stored in the 'users' table of the database

    Attributes:
        user_dict (dict): A dictionary containing the user information

    Methods:
        is_active(): Check if the user is active
        get_id(): Get the user's unique identifier
    """
    def __init__(self, user_dict):
        """
        Initialize a user object

        Args:
            user_dict (dict): A dictionary containing the user information
        """
        self.user_dict = user_dict
    
    def get_id(self):
        return self.user_dict["username"]
    
@login_manager.user_loader
def load_user(username: str) -> User:
    user_dict = current_app.db.users.find_one({"username": username})
    if user_dict is not None:
        return User(user_dict)