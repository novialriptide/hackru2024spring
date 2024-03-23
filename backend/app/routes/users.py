from app.controllers.users import user_exists, create_user, delete_user
from flask import Blueprint, abort, jsonify, request

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["POST"])
def create_user_route():
    """
    Create a new user in the "users" table. The request body should be in JSON format and should contain the following fields:
    {
        "username": "string",
        "password": "string",
    }
    
    Route:
        http://localhost:5000/users

    Returns:
        JSON: A JSON object containing the user's username
    """
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    if user_exists(username):
        abort(400)
    new_user = create_user(username, password)
    return jsonify({"username": new_user["username"]}), 201


@users_bp.route("/users/<b32:username>", methods=["DELETE"])
def delete_user_route(username: str):
    """
    Delete a user from the "users" table

    Route:
        http://localhost:5000/users/<b32:username>

    Args:
        username (str): The username of the user to delete. It is initially encoded using the Base32 encoding scheme

    Returns:
        str: An empty string
    """
    if not user_exists(username):
        abort(404)
    delete_user(username)
    return "", 204