from flask_login import login_user, logout_user, login_required, current_user
from app.controllers.users import user_exists, get_user
from werkzeug.security import check_password_hash
from flask import Blueprint, abort, request

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login_route():
    """
    Log in a user by adding their ID to the session. The request body should be in JSON format and should contain the following fields:
    {
        "username": "string",
        "password": "string"
    }

    Route:
        http://localhost:5000/login

    Returns:
        str: A message indicating that the user has been logged in
    """
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    if not user_exists(username):
        abort(404)
    user = get_user(username)
    if not check_password_hash(user.password, password):
        abort(401)
    login_user(user)
    return f"{user} logged in successfully", 200

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout_route():
    """
    Log out a user by removing their ID from the session

    Route:
        http://localhost:5000/logout

    Returns:
        str: A message indicating that the user has been logged out
    """
    user_repr = current_user.__repr__()
    logout_user()
    return f"{user_repr} logged out successfully", 200



